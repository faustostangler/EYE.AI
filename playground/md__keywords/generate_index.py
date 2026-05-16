import os
import json
import logging
import time
import argparse
from datetime import timedelta
from pathlib import Path
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Suppress verbose HTTP logs from the OpenAI client
logging.getLogger("httpx").setLevel(logging.WARNING)

# Configuration
REFERENCES_DIR = Path('/home/stangler/Documents/Python/EYE.AI/.agents/skills/stangler-blueprint/references')
INDEX_OUTPUT_JSON = REFERENCES_DIR / 'references_index.json'
CANONICAL_MAP = {}

def set_nested(data: dict, keys: list, value: any):
    """Sets a value in a nested dictionary, creating intermediate dicts if needed."""
    for key in keys[:-1]:
        data = data.setdefault(key, {})
    data[keys[-1]] = value

def get_nested(data: dict, keys: list) -> any:
    """Retrieves a value from a nested dictionary. Returns None if path doesn't exist."""
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data

def flatten_index(data: dict, prefix: str = "") -> dict:
    """Flattens a nested index back to rel_path keys for MD generation or internal use."""
    flat = {}
    for key, value in data.items():
        new_path = f"{prefix}/{key}" if prefix else key
        if isinstance(value, dict) and "keywords" not in value:
            flat.update(flatten_index(value, new_path))
        else:
            flat[new_path] = value
    return flat

def save_index(output_path: Path, index_data: dict) -> None:
    """Saves the index data to a JSON file, placing canonical_keywords last.

    This ensures optimal presentation order where the main structural index
    comes first, followed by the global canonical keywords mappings.

    Args:
        output_path: The file path to write the JSON to.
        index_data: The dictionary containing the index and canonical_keywords.
    """
    ordered_data = {}
    if "index" in index_data:
        ordered_data["index"] = index_data["index"]
    if "canonical_keywords" in index_data:
        ordered_data["canonical_keywords"] = index_data["canonical_keywords"]
    
    # Handle any other keys dynamically to avoid dropping data
    for k, v in index_data.items():
        if k not in ("index", "canonical_keywords"):
            ordered_data[k] = v

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ordered_data, f, indent=2, ensure_ascii=False)

# Local LLM Configuration
# Assuming an OpenAI-compatible local server like Ollama, vLLM, or LM Studio
LOCAL_LLM_BASE_URL = os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:11434/v1")
LOCAL_LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "qwen2.5:7b") 

client = OpenAI(base_url=LOCAL_LLM_BASE_URL, api_key="local-llm-key")

def extract_metadata(file_path: Path, chapter: str, canonical_map: dict) -> dict:
    """Extracts document metadata using a dual-stage LLM pipeline.

    The extraction happens in two sequential stages:
    1. Raw Extraction: Extracts key phrases and a one-sentence summary from the text.
    2. Alignment: Leverages the project's existing canonical terminology list
       to identify and propose new terminology to enrich the canonical registry.

    Args:
        file_path: Dynamic path referencing the target document to analyze.
        chapter: Bounded folder or chapter name representing the context of the document.
        canonical_map: Mapped inverted index dictionary containing existing canonical terms.

    Returns:
        dict: A structured dictionary mapping:
            - "keywords": list[str] of extracted primary key terms.
            - "summary": str of one-sentence document summary.
            - "new_canonical": list[str] of newly aligned/proposed canonical keywords.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        content_snippet = content
        
        # STAGE 1: Raw Extraction
        raw_prompt = f"""
Analyze the following technical Markdown document and provide:
1. KEYWORDS: A comma-separated list of the most important technical keywords or key phrases.
2. SUMMARY: A concise, one-sentence summary of the document's core purpose.

Return ONLY the information in this format:
KEYWORDS: <list>
SUMMARY: <sentence>

Text:
{content_snippet}
"""
        
        raw_response = client.chat.completions.create(
            model=LOCAL_LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a precise technical librarian. Extract metadata accurately."},
                {"role": "user", "content": raw_prompt}
            ],
            temperature=0.1,
            max_tokens=500
        )
        
        raw_output = raw_response.choices[0].message.content.strip()
        
        raw_keywords = []
        raw_summary = ""
        
        for line in raw_output.split('\n'):
            if line.startswith('KEYWORDS:'):
                raw_keywords = [k.strip() for k in line.replace('KEYWORDS:', '').split(',') if k.strip()]
            elif line.startswith('SUMMARY:'):
                raw_summary = line.replace('SUMMARY:', '').strip()

        # STAGE 2: Canonical Alignment
        canonical_str = ", ".join(sorted(canonical_map.keys()))
        alignment_prompt = f"""
Given the following raw keywords extracted from a document:
[{", ".join(raw_keywords)}]

And a list of canonical technical keywords for this project:
[{canonical_str}]

Task:
1. Identify distinct new technical terms that should be added to the canonical list.

Return ONLY in this format:
NEW_CANONICAL: <comma-separated new terms to add to the global list>
"""
        
        alignment_response = client.chat.completions.create(
            model=LOCAL_LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a terminology specialist. Standardize keywords and manage a canonical technical list."},
                {"role": "user", "content": alignment_prompt}
            ],
            temperature=0.1,
            max_tokens=300
        )
        
        alignment_output = alignment_response.choices[0].message.content.strip()
        
        new_canonical_terms = []
        
        for line in alignment_output.split('\n'):
            if line.startswith('NEW_CANONICAL:'):
                new_canonical_terms = [k.strip() for k in line.replace('NEW_CANONICAL:', '').split(',') if k.strip()]
            
        return {"keywords": raw_keywords, "summary": raw_summary, "new_canonical": new_canonical_terms}
    except Exception as e:
        logging.error(f"Error processing {file_path.name}: {e}")
        return {"keywords": [], "summary": "Error processing file.", "new_canonical": []}

def main():
    parser = argparse.ArgumentParser(description="Generate a keyword index for reference documents.")
    parser.add_argument("--force", action="store_true", help="Force re-indexing of all files, ignoring mtime.")
    args = parser.parse_args()

    if not REFERENCES_DIR.exists():
        logging.error(f"References directory not found: {REFERENCES_DIR}")
        return
        
    index_data = {"canonical_keywords": {}, "index": {}}
    md_files = sorted([f for f in REFERENCES_DIR.rglob('*.md')])
    total_files = len(md_files)
    
    # Load existing index for incremental updates
    if INDEX_OUTPUT_JSON.exists():
        try:
            with open(INDEX_OUTPUT_JSON, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                if "index" not in loaded_data and "canonical_keywords" not in loaded_data:
                    index_data["index"] = loaded_data
                else:
                    index_data = loaded_data
        except Exception as e:
            logging.warning(f"Could not load existing JSON index: {e}")

    global CANONICAL_MAP
    canonical_data = index_data.get("canonical_keywords", {})
    if isinstance(canonical_data, list):
        logging.info("Migrating flat list of canonical keywords to inverted index dictionary...")
        CANONICAL_MAP = {kw: [] for kw in canonical_data}
    else:
        CANONICAL_MAP = canonical_data

    # Populate CANONICAL_MAP with all previously extracted keywords from cached files
    flat_data = flatten_index(index_data["index"])
    added_count = 0
    for rel_path, data in flat_data.items():
        parts = rel_path.split('/')
        chapter = parts[0] if len(parts) > 1 else "Root"
        for kw in data.get('keywords', []):
            if kw not in CANONICAL_MAP:
                CANONICAL_MAP[kw] = []
                added_count += 1
            if chapter not in CANONICAL_MAP[kw]:
                CANONICAL_MAP[kw].append(chapter)

    # Sort the mapping keys and lists
    sorted_map = {}
    for kw in sorted(CANONICAL_MAP.keys()):
        sorted_map[kw] = sorted(list(set(CANONICAL_MAP[kw])))
    CANONICAL_MAP = sorted_map
    index_data["canonical_keywords"] = CANONICAL_MAP

    if added_count > 0:
        try:
            save_index(INDEX_OUTPUT_JSON, index_data)
            logging.info(f"Loaded and merged {added_count} keywords from existing index into canonical map (Total: {len(CANONICAL_MAP)}).")
        except Exception as e:
            logging.error(f"Failed to sync json file at startup: {e}")

    logging.info(f"Found {len(md_files)} markdown files to process.")
    
    start_time = time.perf_counter()
    current_chapter = None
    
    # Process files sequentially to respect local LLM constraints
    for i, file_path in enumerate(md_files, 1):
        rel_path_obj = file_path.relative_to(REFERENCES_DIR)
        rel_path = rel_path_obj.as_posix()
        path_parts = list(rel_path_obj.parts)
        
        # Chapter tracking header
        chapter = path_parts[0] if len(path_parts) > 1 else "Root"
        if chapter != current_chapter:
            logging.info(f"--- processando {chapter} ---")
            current_chapter = chapter
        
        # Check modified time for real incremental updates (nested lookup)
        mtime = file_path.stat().st_mtime
        existing_meta = get_nested(index_data["index"], path_parts)
        if not args.force and existing_meta and existing_meta.get('mtime') == mtime:
            # Re-ensure skipped document keywords exist in CANONICAL_MAP under this chapter
            for kw in existing_meta.get('keywords', []):
                if kw not in CANONICAL_MAP:
                    CANONICAL_MAP[kw] = []
                if chapter not in CANONICAL_MAP[kw]:
                    CANONICAL_MAP[kw].append(chapter)
            
            # For skipped files, calculate progress instantly
            elapsed_sec = time.perf_counter() - start_time
            avg_time_per_file = elapsed_sec / i if i > 0 else 0
            remaining_files = total_files - i
            eta_sec = avg_time_per_file * remaining_files
            elapsed_str = str(timedelta(seconds=int(elapsed_sec)))
            eta_str = str(timedelta(seconds=int(eta_sec)))
            total_time_str = str(timedelta(seconds=int(elapsed_sec + eta_sec)))
            percent = (i / total_files) * 100
            progress_prefix = f"[{i}+{remaining_files}] [{percent:.2f}%] {elapsed_str}+{eta_str}={total_time_str}"
            logging.info(f"{progress_prefix} {file_path.name[:35]}...")
            continue
            
        metadata = extract_metadata(file_path, chapter, CANONICAL_MAP)

        if metadata["keywords"]:
            set_nested(index_data["index"], path_parts, {
                "keywords": metadata["keywords"],
                "summary": metadata["summary"],
                "mtime": mtime
            })
            
            # Ensure extracted keywords are in the global map under this chapter
            for kw in metadata["keywords"]:
                if kw not in CANONICAL_MAP:
                    CANONICAL_MAP[kw] = []
                if chapter not in CANONICAL_MAP[kw]:
                    CANONICAL_MAP[kw].append(chapter)
            
            # Ensure newly proposed canonical terms are in the global map under this chapter
            for term in metadata.get("new_canonical", []):
                if term not in CANONICAL_MAP:
                    CANONICAL_MAP[term] = []
                if chapter not in CANONICAL_MAP[term]:
                    CANONICAL_MAP[term].append(chapter)
            
        # Ensure canonical map is sorted before writing
        sorted_map = {}
        for kw in sorted(CANONICAL_MAP.keys()):
            sorted_map[kw] = sorted(list(set(CANONICAL_MAP[kw])))
        CANONICAL_MAP = sorted_map
        index_data["canonical_keywords"] = CANONICAL_MAP
        
        # ALWAYS save progress to capture global CANONICAL_MAP updates
        save_index(INDEX_OUTPUT_JSON, index_data)
        
        # Generate timing after processing is complete
        elapsed_sec = time.perf_counter() - start_time
        avg_time_per_file = elapsed_sec / i if i > 0 else 0
        remaining_files = total_files - i
        eta_sec = avg_time_per_file * remaining_files
        elapsed_str = str(timedelta(seconds=int(elapsed_sec)))
        eta_str = str(timedelta(seconds=int(eta_sec)))
        total_time_str = str(timedelta(seconds=int(elapsed_sec + eta_sec)))
        percent = (i / total_files) * 100
        progress_prefix = f"[{i}+{remaining_files}] [{percent:.2f}%] {elapsed_str}+{eta_str}={total_time_str}"
        
        logging.info(f"{progress_prefix} {file_path.name[:35]}...")
        
    # Re-sort and perform a final write to guarantee all updates (especially in incremental skip runs) are written to the JSON file
    sorted_map = {}
    for kw in sorted(CANONICAL_MAP.keys()):
        sorted_map[kw] = sorted(list(set(CANONICAL_MAP[kw])))
    CANONICAL_MAP = sorted_map
    index_data["canonical_keywords"] = CANONICAL_MAP
    
    try:
        save_index(INDEX_OUTPUT_JSON, index_data)
        logging.info(f"Indexing complete! Successfully synced and saved inverted keyword index to {INDEX_OUTPUT_JSON}")
    except Exception as e:
        logging.error(f"Failed to write final JSON index: {e}")

if __name__ == "__main__":
    main()
