import sys
try:
    import os
    import json
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_chroma import Chroma
    from langchain_community.llms import Ollama
    from langchain_core.prompts import PromptTemplate
    print("SUCCESS: All imports passed.")
except ImportError as e:
    print(f"FAILURE: {e}")
    sys.exit(1)
except Exception as e:
    print(f"UNEXPECTED ERROR: {e}")
    sys.exit(1)
