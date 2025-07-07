# chroma_client.py

import os
import chromadb
from chromadb.config import Settings

#Absolute path to your embeddings folder
base_dir = os.path.dirname(os.path.abspath(__file__))
persist_path = os.path.join(base_dir, "embeddings/chroma")

print(persist_path)
#Create one global client with correct settings
client = chromadb.Client(Settings(persist_directory=persist_path))
#client.persist(persist_path)

