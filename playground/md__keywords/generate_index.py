import os
import json
import logging
import time
import argparse
import re
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

    # Handle any other keys dynamically to avoid dropping data
    for k, v in index_data.items():
        if k not in ("index", "canonical_keywords"):
            ordered_data[k] = v

    # canonical_keywords always last
    if "canonical_keywords" in index_data:
        ordered_data["canonical_keywords"] = index_data["canonical_keywords"]
    

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ordered_data, f, indent=2, ensure_ascii=False)

# Local LLM Configuration
# Assuming an OpenAI-compatible local server like Ollama, vLLM, or LM Studio
LOCAL_LLM_BASE_URL = os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:11434/v1")
LOCAL_LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "qwen2.5:7b") 

client = OpenAI(base_url=LOCAL_LLM_BASE_URL, api_key="local-llm-key")

def split_camel_case(s: str) -> str:
    """Splits CamelCase and PascalCase into Title Case with spaces."""
    s = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)
    s = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', s)
    return s

def normalize_to_canonical(keyword: str, canonical_map: dict) -> str:
    """Deterministic post-LLM normalization against canonical keyword SSOT.

    WHY: LLMs (especially small local models) are non-deterministic for exact
    string matching. This function applies deterministic rules AFTER LLM
    extraction to collapse trivial variations. The canonical_map itself is
    the only source of truth — no manual exception lists needed.

    Matching priority:
        1. Exact match (fast path)
        2. Case-insensitive match ("Jira ticket" → "Jira Ticket")
        3. Singular/plural match ("Generic Subdomain" → "Generic Subdomains")
    """
    kw = keyword.strip()
    kw = split_camel_case(kw)

    # 1. Exact match
    if kw in canonical_map:
        return kw

    kw_lower = kw.lower()

    # 2. Case-insensitive match
    for canonical_key in canonical_map:
        if canonical_key.lower() == kw_lower:
            return canonical_key

    # 3. Singular/plural normalization (strip trailing 's' for comparison)
    for canonical_key in canonical_map:
        ck_lower = canonical_key.lower()
        if (
            kw_lower + 's' == ck_lower
            or kw_lower.rstrip('s') == ck_lower.rstrip('s')
        ):
            return canonical_key

    # No match — return as-is (becomes new canonical entry)
    return kw


def extract_metadata(file_path: Path, chapter: str, canonical_map: dict) -> dict:
    """Extracts document metadata using a dual-stage LLM pipeline.

    Stage 1 (Raw Extraction): Extracts named technical concepts and a summary.
    Stage 2 (Normalization & Alignment): Uses the canonical keyword list as SSOT
    to normalize raw keywords to their canonical forms and propose new terms.
    All case/spelling normalization is delegated to the LLM, eliminating the
    need for manual acronym or compound-word exception lists.

    Args:
        file_path: Dynamic path referencing the target document to analyze.
        chapter: Bounded folder or chapter name representing the context of the document.
        canonical_map: Mapped inverted index dictionary containing existing canonical terms.

    Returns:
        dict: A structured dictionary mapping:
            - "keywords": list[str] of normalized canonical key terms.
            - "summary": str of one-sentence document summary.
            - "new_canonical": list[str] of newly proposed canonical keywords.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        content_snippet = content
        
        # STAGE 1: Raw Extraction — Restrictive prompt for named concepts only
        raw_prompt = f"""
Extract ONLY specific, named technical concepts from this document.

Rules for KEYWORDS:
- Each keyword MUST be a proper noun, named methodology, named pattern, named tool, or specific technical term.
  GOOD examples: "Domain-Driven Design", "Hexagonal Architecture", "Team Topologies", "Bounded Context", "Event Storming", "Conway's Law"
  BAD examples: "collaboration", "clarity", "implementation", "organization", "boundaries", "speed", "cost", "quality"
- Use the FULL canonical name of concepts (e.g., "Domain-Driven Design" not "DDD").
- Do NOT use PascalCase or camelCase. ALWAYS separate words with spaces (e.g., "Event Storming", NOT "EventStorming").
- Do NOT include generic adjectives, verbs, or descriptive phrases.
- Return all relevant keywords per document.

1. KEYWORDS: A comma-separated list of specific named technical concepts.
2. SUMMARY: A concise, one-sentence summary of the document's core purpose.

Return ONLY in this format:
KEYWORDS: <list>
SUMMARY: <sentence>

Text:
{content_snippet}
"""
        
        raw_response = client.chat.completions.create(
            model=LOCAL_LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a precise technical librarian specializing in software engineering taxonomy. Extract ONLY named concepts, methodologies, patterns, and tools. Never extract generic words."},
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

        # STAGE 2: Normalization against canonical SSOT (LLM for semantic matching)
        canonical_str = ", ".join(sorted(canonical_map.keys()))
        alignment_prompt = f"""
For each raw keyword below, check if it matches (same concept, different casing or spelling) any term in the canonical list. If it matches, use the EXACT canonical form. If no match exists, keep the keyword in proper Title Case, with spaces between words. NEVER remove spaces between words (e.g., output "Event Storming", NOT "EventStorming").

Raw keywords from document:
[{", ".join(raw_keywords)}]

Existing canonical keywords (SSOT — use these exact forms when a match exists):
[{canonical_str}]

Return ONLY in this exact format (one line):
NORMALIZED: <comma-separated list of ALL keywords, each mapped to canonical form or Title Case>
"""
        
        alignment_response = client.chat.completions.create(
            model=LOCAL_LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a terminology normalization specialist. Map raw keywords to their existing canonical forms using exact string matching. Preserve the exact casing and spelling of canonical terms. For new terms, use proper Title Case with spaces between words (e.g. 'Modular Monoliths', NOT 'ModularMonoliths')."},
                {"role": "user", "content": alignment_prompt}
            ],
            temperature=0.1,
            max_tokens=300
        )
        
        alignment_output = alignment_response.choices[0].message.content.strip()
        
        normalized_keywords = raw_keywords  # Fallback to raw if parsing fails
        
        for line in alignment_output.split('\n'):
            if line.startswith('NORMALIZED:'):
                parsed = [k.strip() for k in line.replace('NORMALIZED:', '').split(',') if k.strip()]
                if parsed:
                    normalized_keywords = parsed

        # STAGE 3: Deterministic post-processing against canonical SSOT
        # WHY: LLM output is probabilistic; this collapses casing/plural drift
        normalized_keywords = [
            normalize_to_canonical(kw, canonical_map) for kw in normalized_keywords
        ]
        # Deduplicate after normalization (two raw keywords may collapse to same canonical)
        normalized_keywords = list(dict.fromkeys(normalized_keywords))

        return {"keywords": normalized_keywords, "summary": raw_summary}
    except Exception as e:
        logging.error(f"Error processing {file_path.name}: {e}")
        return {"keywords": [], "summary": "Error processing file."}

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
            logging.info(f"--- Chapter {chapter} ---")
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
            
            # WHY: new canonical detection is deterministic — any keyword
            # not already in CANONICAL_MAP was auto-added above (L361-365)
            
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
