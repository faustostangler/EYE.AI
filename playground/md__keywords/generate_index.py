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
INDEX_OUTPUT_MD = REFERENCES_DIR / 'references_index.md'
CANONICAL_KEYWORDS_FILE = REFERENCES_DIR / 'canonical_keywords.json'

def load_canonical_list() -> list:
    if CANONICAL_KEYWORDS_FILE.exists():
        try:
            with open(CANONICAL_KEYWORDS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except Exception as e:
            return []
    return []


CANONICAL_LIST = load_canonical_list()

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

# Local LLM Configuration
# Assuming an OpenAI-compatible local server like Ollama, vLLM, or LM Studio
LOCAL_LLM_BASE_URL = os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:11434/v1")
LOCAL_LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "qwen2.5:7b") 

client = OpenAI(base_url=LOCAL_LLM_BASE_URL, api_key="local-llm-key")

def extract_metadata(file_path: Path) -> dict:
    """Extracts metadata using a dual-stage LLM approach for canonical alignment."""
    try:
        content = file_path.read_text(encoding='utf-8')
        # content_snippet = content[:6000] # context limit
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
            max_tokens=250
        )
        
        raw_output = raw_response.choices[0].message.content.strip()
        
        raw_keywords = []
        summary = ""
        
        for line in raw_output.split('\n'):
            if line.startswith('KEYWORDS:'):
                raw_keywords = [k.strip() for k in line.replace('KEYWORDS:', '').split(',') if k.strip()]
            elif line.startswith('SUMMARY:'):
                summary = line.replace('SUMMARY:', '').strip()

        # STAGE 2: Canonical Alignment
        canonical_str = ", ".join(CANONICAL_LIST)
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
        
        # Update global canonical list
        if new_canonical_terms:
            for term in new_canonical_terms:
                if term not in CANONICAL_LIST:
                    CANONICAL_LIST.append(term)
            CANONICAL_LIST.sort()
            
        return {"keywords": raw_keywords, "summary": summary}
    except Exception as e:
        logging.error(f"Error processing {file_path.name}: {e}")
        return {"keywords": [], "summary": "Error processing file."}

def generate_md_index(index_data: dict, output_path: Path):
    """Generates a Markdown index with an inverted keyword-to-chapter section."""
    logging.info(f"Updating Markdown Index: {output_path.name}")
    try:
        flat_data = flatten_index(index_data)
        
        # Build inverted index: keyword -> set of chapters (folders)
        inverted_index = {}
        for rel_path, data in flat_data.items():
            # Chapter is the first part of the path
            chapter = rel_path.split('/')[0]
            for kw in data.get('keywords', []):
                if kw not in inverted_index:
                    inverted_index[kw] = set()
                inverted_index[kw].add(chapter)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# References Keyword Index\n\n")
            
            f.write("## 1. Inverted Keyword Index\n")
            f.write("Keyword-based mapping to document chapters.\n\n")
            for kw in sorted(inverted_index.keys()):
                chapters = sorted(list(inverted_index[kw]))
                f.write(f"- **{kw}**: {json.dumps(chapters, ensure_ascii=False)}\n")
            
            f.write("\n---\n\n")
            f.write("## 2. Document Details\n")
            f.write("Detailed metadata for each document.\n\n")
            for rel_path, data in sorted(flat_data.items()):
                keywords_str = ", ".join(data.get('keywords', []))
                summary = data.get('summary', 'No summary available.')
                f.write(f"### {rel_path}\n")
                f.write(f"- **Summary**: {summary}\n")
                f.write(f"- **Keywords**: {keywords_str}\n\n")
    except Exception as e:
        logging.error(f"Failed to generate Markdown index: {e}")
def main():
    parser = argparse.ArgumentParser(description="Generate a keyword index for reference documents.")
    parser.add_argument("--force", action="store_true", help="Force re-indexing of all files, ignoring mtime.")
    args = parser.parse_args()

    if not REFERENCES_DIR.exists():
        logging.error(f"References directory not found: {REFERENCES_DIR}")
        return
        
    index_data = {}
    # Find all MD files but skip the index itself if it's in the same folder. Sort them for consistent chapter grouping.
    md_files = sorted([f for f in REFERENCES_DIR.rglob('*.md') if f.name != INDEX_OUTPUT_MD.name])
    
    # Load existing index for incremental updates
    if INDEX_OUTPUT_JSON.exists():
        try:
            with open(INDEX_OUTPUT_JSON, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
        except Exception as e:
            logging.warning(f"Could not load existing JSON index: {e}")

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
        
        # Calculate timing
        elapsed_sec = time.perf_counter() - start_time
        avg_time_per_file = elapsed_sec / i if i > 0 else 0
        total_files = len(md_files)
        remaining_files = total_files - i
        eta_sec = avg_time_per_file * remaining_files
        
        # Format strings
        elapsed_str = str(timedelta(seconds=int(elapsed_sec)))
        eta_str = str(timedelta(seconds=int(eta_sec)))
        total_time_str = str(timedelta(seconds=int(elapsed_sec + eta_sec)))
        
        percent = (i / total_files) * 100
        progress_prefix = f"[{i}+{remaining_files} {percent:.2f}%] [{elapsed_str}+{eta_str}={total_time_str}]"
        
        # Check modified time for real incremental updates (nested lookup)
        mtime = file_path.stat().st_mtime
        existing_meta = get_nested(index_data, path_parts)
        if not args.force and existing_meta and existing_meta.get('mtime') == mtime:
            logging.info(f"{progress_prefix} Skipping (unchanged): {file_path.name}")
            continue
            
        logging.info(f"{progress_prefix} {file_path.name}")
        metadata = extract_metadata(file_path)
        
        if metadata["keywords"]:
            set_nested(index_data, path_parts, {
                "keywords": metadata["keywords"],
                "summary": metadata["summary"],
                "mtime": mtime
            })
            
        # ALWAYS save progress to capture global CANONICAL_LIST updates
        with open(INDEX_OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        
        with open(CANONICAL_KEYWORDS_FILE, 'w', encoding='utf-8') as f:
            json.dump(CANONICAL_LIST, f, indent=2, ensure_ascii=False)
        
        if i % 1 == 0 or i == len(md_files): 
            generate_md_index(index_data, INDEX_OUTPUT_MD)
            
    # Final generation
    generate_md_index(index_data, INDEX_OUTPUT_MD)
    logging.info(f"Indexing complete! Saved to {INDEX_OUTPUT_MD}")

if __name__ == "__main__":
    main()
