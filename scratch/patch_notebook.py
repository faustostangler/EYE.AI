import json

path = "/home/stangler/Documents/Python/EYE.AI/playground/ingestion.ipynb"
with open(path, "r") as f:
    nb = json.load(f)

# Fix Cell 1 (Installation)
cell1 = nb["cells"][0]
cell1["source"] = [
    "!uv pip install langchain langchain-community langchain-core langchain-chroma langchain-huggingface langchain-ollama sentence-transformers pypdf ipywidgets widgetsnbextension"
]
cell1["outputs"] = []
cell1["execution_count"] = None

# Fix Cell 2 (Imports)
cell2 = nb["cells"][1]
cell2["source"] = [
    "import os\n",
    "import json\n",
    "from langchain_community.document_loaders import TextLoader\n",
    "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
    "from langchain_huggingface import HuggingFaceEmbeddings\n",
    "from langchain_chroma import Chroma\n",
    "from langchain_ollama import OllamaLLM\n",
    "from langchain_core.prompts import PromptTemplate"
]
cell2["outputs"] = []
cell2["execution_count"] = None

# Fix Cell 3 (Logic & Model Name)
cell3 = nb["cells"][2]
source = cell3["source"]

# Update MODEL_NAME
for i, line in enumerate(source):
    if "MODEL_NAME =" in line:
        source[i] = "MODEL_NAME = \"gemma:2b\" \n"
    if "llm = Ollama(model=MODEL_NAME, format=\"json\")" in line:
        source[i] = line.replace("Ollama(", "OllamaLLM(")

cell3["source"] = source
cell3["outputs"] = []
cell3["execution_count"] = None

with open(path, "w") as f:
    json.dump(nb, f, indent=1)

print("Notebook patched successfully with modern LangChain packages.")
