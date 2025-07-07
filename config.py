import os
# config.py
# DB_PATH = "db/transactions.db"
# INIT_SQL_PATH = "init/init.sql"
#
#
# === PATHS ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DB
SQLITE_DB_PATH = os.path.join(BASE_DIR, "transactions.db")
CREATE_SQL_PATH = os.path.join(BASE_DIR, "init", "init.sql")
SEED_SQL_PATH = os.path.join(BASE_DIR, "init", "seed_data.sql")

# Chroma
CHROMA_PERSIST_PATH = os.path.join(BASE_DIR, "embeddings", "chroma")
CHROMA_COLLECTION_NAME = "schema_docs"

# Data files
DOCUMENTS_PATH = os.path.join(BASE_DIR, "data", "combined_document.json")

# Sentence transformer model
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# LLM settings
LLM_MODEL = "mistral"
LLM_PROVIDER = "ollama"  # or "openrouter", "replicate"
OLLAMA_BASE_URL = "http://localhost:11434"

# Retrieval
TOP_K_RESULTS = 3

