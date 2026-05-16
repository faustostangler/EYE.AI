import requests
import json
import os

# Configurações extraídas da nossa investigação
BASE_URL = "https://api.voa.health/api/v1"
TOKEN = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4ODQxNzQ5LCJpYXQiOjE3Nzg4MDQ5NDIsImp0aSI6ImFkYWMzOWFmMTFkZjRiZDE5OGM5MWI1NjA4OTZlNjIzIiwidXNlcl9pZCI6IjdkZmU5YmI5LTNjNzQtNDJiNy04MmIyLWVmZjE2NTU4MjEzYiIsInJldm9rZSI6IjIyN0YyMzQzQUM4REY1NjQ5MzkxM0IzOTg5QUQ1NDFEIn0.UgQ6XIoHbSZ3mroP4-v-pZLYiCKiUjqmoljw1hRcmovJGNNGkrBAovGFgII3pz4dCSBUqRzxmiPTZjmwVECBOw"

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
    "x-voa-app": "voa-frontend/2.0.0"
}

def get_profile():
    """Retorna os detalhes do médico logado."""
    print("🚀 Buscando perfil do médico...")
    response = requests.get(f"{BASE_URL}/user/", headers=headers)
    return response.json()

def list_ehrs(page=1):
    """Lista os atendimentos (EHRs) paginados."""
    print(f"📄 Buscando atendimentos (Página {page})...")
    response = requests.get(f"{BASE_URL}/ehr/?page={page}", headers=headers)
    return response.json()

def export_all_data():
    """Faz um dump completo dos atendimentos para um arquivo JSON local."""
    all_ehrs = []
    page = 1
    
    while True:
        data = list_ehrs(page)
        results = data.get("results", [])
        if not results:
            break
        all_ehrs.extend(results)
        if not data.get("next"):
            break
        page += 1
    
    filename = "playground/voa/export_atendimentos.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_ehrs, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Exportação concluída! {len(all_ehrs)} atendimentos salvos em {filename}")

if __name__ == "__main__":
    profile = get_profile()
    print(f"👤 Logado como: {profile.get('name')} ({profile.get('specialty')})")
    
    # Descomente para rodar a exportação completa
    export_all_data()
