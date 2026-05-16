import json
import os
import re
from pathlib import Path

# Configuração de Caminhos (SSOT)
BASE_DIR = Path(__file__).parent
base_output_dir = BASE_DIR / "references"
base_output_dir.mkdir(exist_ok=True)

# Lista dos arquivos JSON de origem
json_files = [
    BASE_DIR / "1.3. Knowledge Management & Documentation-backup-2026-05-16.json",
]

def sanitize_filename(title):
    # Remove caracteres inválidos para nomes de arquivos e limita o tamanho
    sanitized = re.sub(r'[\\/*?:"<>|]', "", str(title))
    return sanitized[:150].strip()

print(f"🚀 Iniciando extração. Base: {base_output_dir.absolute()}")

for file_path in json_files:
    if file_path.exists():
        print(f"📄 Processando arquivo: {file_path.name}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Extração de metadados do nível raiz do JSON
        exported_at = data.get("exportedAt", "N/A")
        notebook_title = data.get("notebook", {}).get("title", "N/A")
        
        # Criação do subdiretório específico do notebook
        safe_notebook_dir = sanitize_filename(notebook_title)
        notebook_dir = base_output_dir / safe_notebook_dir
        notebook_dir.mkdir(exist_ok=True)
        
        sources = data.get("sources", [])
        print(f"   Found {len(sources)} sources. Saving to: references/{safe_notebook_dir}/")
        
        # Iteração sobre cada fonte presente na lista "sources"
        for source in sources:
            title = source.get("title", "Untitled")
            url = source.get("url", "N/A")
            source_type = source.get("sourceType", "N/A")
            content = source.get("content", "")
            
            safe_title = sanitize_filename(title)
            if not safe_title:
                safe_title = f"Untitled_{source.get('id', 'N_A')}"
                
            md_filename = notebook_dir / f"{safe_title}.md"
            
            # Montagem do conteúdo Markdown
            md_content = f"""---
name: {title}
keywords: (placeholder)
metadata:
  url: {url}
  source: {source_type}
  date: {exported_at}
  notebook: {notebook_title}
---
{content}
"""
            # Escrita no arquivo .md correspondente
            with open(md_filename, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)

print(f"\n✅ Processamento concluído com sucesso!")