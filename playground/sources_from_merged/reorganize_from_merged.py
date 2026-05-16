import os
import re
import shutil

def sanitize_name(name):
    """Sanitize filename by removing illegal or problematic characters."""
    # Common illegal characters for most filesystems
    sanitized = re.sub(r'[\\/*?:"<>|]', '_', name.strip())
    # Optional: replace multiple underscores with a single one
    sanitized = re.sub(r'_+', '_', sanitized)
    return sanitized

def process():
    # Define target directory as the one containing this script
    target_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get all .md files in the target directory
    files = [f for f in os.listdir(target_dir) if f.endswith('.md')]
    
    if not files:
        print(f"No valid .md files found in: {target_dir}")
        return

    # Flexible sorting logic: handles "1-Folder 01.md" or "Folder 01.md"
    def get_sort_key(f):
        # If starts with "number-", use that number as primary sort
        prefix_match = re.match(r'^(\d+)-', f)
        if prefix_match:
            return int(prefix_match.group(1))
        # Otherwise, use the number at the end before .md (e.g., "01")
        suffix_match = re.search(r'(\d+)\.md$', f)
        if suffix_match:
            return int(suffix_match.group(1))
        # Fallback to first number found or 0
        nums = re.findall(r'\d+', f)
        return int(nums[0]) if nums else 0

    try:
        files.sort(key=get_sort_key)
    except Exception as e:
        files.sort()

    # Flexible folder name extraction
    first_file = files[0]
    # Pattern 1: "1-FolderName 01.md"
    match1 = re.search(r'^\d+-(.*?) \d+\.md', first_file)
    # Pattern 2: "FolderName 01.md"
    match2 = re.search(r'^(.*?)\s\d+\.md', first_file)
    
    if match1:
        folder_name = sanitize_name(match1.group(1))
    elif match2:
        folder_name = sanitize_name(match2.group(1))
    else:
        folder_name = "processed_md"
    
    # Destination is now in a 'references' subfolder relative to target_dir
    dest_folder = os.path.join(target_dir, "references", folder_name)
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Step 1: Sequential carry-over of the last item
    for i in range(len(files) - 1):
        file_curr = files[i]
        file_next = files[i+1]
        file_curr_path = os.path.join(target_dir, file_curr)
        file_next_path = os.path.join(target_dir, file_next)
        
        with open(file_curr_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Find the last "Source:" line to identify the last item
        last_source_idx = -1
        for idx, line in enumerate(lines):
            if line.startswith('Source:'):
                last_source_idx = idx
        
        if last_source_idx != -1:
            # The item to move starts at the last "Source:"
            to_move = lines[last_source_idx:]
            remaining = lines[:last_source_idx]
            
            # Save the truncated current file
            with open(file_curr_path, 'w', encoding='utf-8') as f:
                f.writelines(remaining)
            
            # Prepend the item to the next file
            with open(file_next_path, 'r', encoding='utf-8') as f:
                next_content = f.read()
            
            with open(file_next_path, 'w', encoding='utf-8') as f:
                f.writelines(to_move)
                f.write(next_content)

    # Step 2: Move and rename all files to the destination folder
    for f in files:
        src_path = os.path.join(target_dir, f)
        
        # Remove only the leading index and dash if it exists
        clean_name = re.sub(r'^\d+-', '', f)
        # Sanitize the filename (keeping extension)
        base, ext = os.path.splitext(clean_name)
        new_name = sanitize_name(base) + ext
        
        dest_path = os.path.join(dest_folder, new_name)
        
        # Handle overwrite if file exists
        if os.path.exists(dest_path):
            os.remove(dest_path)
        shutil.move(src_path, dest_path)

if __name__ == "__main__":
    process()
