import json
import os

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# PoC: Visual RAG com ColPali (SOTA)\n",
                "\n",
                "**Objetivo**: Validar a ingestão end-to-end baseada em visão para documentos clínicos complexos (tabelas, fluxogramas, ECGs) usando **ColPali** através da biblioteca `Byaldi`.\n",
                "\n",
                "**Restrições Arquiteturais Mapeadas**:\n",
                "1. **VRAM (6GB Max)**: O modelo original `vidore/colpali-v1.2` (baseado no PaliGemma de 3B parâmetros) exige ~6GB em bf16. Para rodar na RTX 2060 de forma segura, faremos quantização usando `bitsandbytes` (`load_in_4bit=True`), derrubando o uso para ~2.5GB.\n",
                "2. **Espaço em Disco**: O paradigma de *Late Interaction* (ColBERT) salva múltiplos vetores por página. O custo de armazenamento é de cerca de **15 a 20 MB por página de PDF**. Indexar bibliotecas imensas requer planejamento de infraestrutura (NVMe ou buckets de baixo custo).\n",
                "3. **Tamanho do Batch**: Processaremos a indexação de forma unitária (batch pequeno) para não estourar a VRAM durante a geração de vetores."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import os\n",
                "import torch\n",
                "from IPython.display import Image, display\n",
                "from byaldi import RAGMultiModalModel\n",
                "\n",
                "print(f\"CUDA Disponível: {torch.cuda.is_available()}\")\n",
                "if torch.cuda.is_available():\n",
                "    print(f\"Dispositivo: {torch.cuda.get_device_name(0)}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 1. Inicialização do Modelo (Gestão de Memória)\n",
                "Injetando os parâmetros do HuggingFace para forçar a quantização 4-bit na GPU."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Configurações para proteger a VRAM de 6GB\n",
                "model_kwargs = {\n",
                "    \"load_in_4bit\": True,\n",
                "    \"device_map\": \"auto\"\n",
                "}\n",
                "\n",
                "print(\"Carregando ColPali (PaliGemma 3B) em 4-bits... Isso pode levar um tempo no primeiro download.\")\n",
                "RAG = RAGMultiModalModel.from_pretrained(\n",
                "    \"vidore/colpali-v1.2\",\n",
                "    verbose=1,\n",
                "    model_kwargs=model_kwargs\n",
                ")\n",
                "print(\"Modelo carregado com sucesso!\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 2. Mock & Ingestão Visual\n",
                "Aqui, ao invés de extrair texto, o modelo vai 'tirar uma foto' da página e extrair as feições semânticas da imagem diretamente."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Setup de teste: Criar um PDF simulado caso não tenha nenhum\n",
                "from fpdf import FPDF\n",
                "\n",
                "pdf_teste = \"protocolo_visual.pdf\"\n",
                "if not os.path.exists(pdf_teste):\n",
                "    pdf = FPDF()\n",
                "    pdf.add_page()\n",
                "    pdf.set_font(\"Arial\", size=12)\n",
                "    pdf.cell(200, 10, txt=\"Protocolo de Dor Toracica Institucional - FLUXOGRAMA\", ln=1, align='C')\n",
                "    pdf.cell(200, 10, txt=\"Se Supra de ST no ECG -> Encaminhar para Cateterismo imediato.\", ln=1, align='L')\n",
                "    pdf.cell(200, 10, txt=\"Dose de Ataque: AAS 300mg + Ticagrelor 180mg\", ln=1, align='L')\n",
                "    pdf.output(pdf_teste)\n",
                "    print(f\"PDF mock '{pdf_teste}' gerado.\")\n",
                "\n",
                "# Ingestão (Indexação)\n",
                "INDEX_NAME = \"poc_dor_toracica\"\n",
                "\n",
                "print(f\"Indexando o documento visualmente... (Espaço estimado: ~15MB/pág)\")\n",
                "RAG.index(\n",
                "    input_path=pdf_teste,\n",
                "    index_name=INDEX_NAME,\n",
                "    store_collection_with_index=True, # Salva metadados da imagem no índice para visualização\n",
                "    overwrite=True\n",
                ")\n",
                "print(\"Indexação concluída! Os tensores foram salvos no diretório .byaldi/\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 3. Recuperação Visual (Late Interaction)\n",
                "Nós fazemos uma pergunta em texto. O ColBERT vai buscar quais \"patches\" da imagem melhor respondem à pergunta."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "pergunta = \"Qual a dose de ataque para IAM com Supra?\"\n",
                "print(f\"Pesquisando: '{pergunta}'\")\n",
                "\n",
                "# Busca (k=1 pois temos só 1 página mockada)\n",
                "resultados = RAG.search(pergunta, k=1)\n",
                "\n",
                "print(\"\\n=== Resultado ===\")\n",
                "for res in resultados:\n",
                "    print(f\"Documento: {res.doc_id}\")\n",
                "    print(f\"Score Semântico Visual (ColBERT): {res.score:.2f}\")\n",
                "    print(f\"Base64 Image Reference presente: {'base64' in res.metadata}\")\n",
                "    \n",
                "    # Para debugar e mostrar ao médico de onde veio a info\n",
                "    if 'base64' in res.metadata:\n",
                "        from IPython.display import display, HTML\n",
                "        display(HTML(f'<img src=\"data:image/jpeg;base64,{res.metadata[\"base64\"]}\" width=\"400\"/>'))\n"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": ".venv",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.13"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("/home/stangler/Documents/Python/EYE.AI/playground/colpali_poc.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("Notebook gerado em playground/colpali_poc.ipynb")
