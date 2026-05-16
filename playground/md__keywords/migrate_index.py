import json
from pathlib import Path

INDEX_JSON = Path('/home/stangler/Documents/Python/EYE.AI/.agents/skills/stangler-blueprint/references_index.json')

def set_nested(data, keys, value):
    for key in keys[:-1]:
        data = data.setdefault(key, {})
    data[keys[-1]] = value

def migrate():
    if not INDEX_JSON.exists():
        print("No index file found.")
        return

    with open(INDEX_JSON, 'r', encoding='utf-8') as f:
        flat_data = json.load(f)

    # Check if already migrated (heuristics: first key doesn't contain '/')
    first_key = next(iter(flat_data.keys()), "")
    if first_key and '/' not in first_key and isinstance(flat_data[first_key], dict) and "keywords" not in flat_data[first_key]:
        print("Already seems hierarchical.")
        return

    nested_data = {}
    for rel_path, meta in flat_data.items():
        if isinstance(meta, dict) and "keywords" in meta:
            parts = rel_path.split('/')
            set_nested(nested_data, parts, meta)
        else:
            # Already nested or weird entry
            nested_data[rel_path] = meta

    with open(INDEX_JSON, 'w', encoding='utf-8') as f:
        json.dump(nested_data, f, indent=2, ensure_ascii=False)
    print("Migration complete!")

if __name__ == "__main__":
    migrate()
