# embedding_chroma.py
import json
import os
import chromadb
#from chromadb.config import Settings
from modules.chroma_client import client
from sentence_transformers import SentenceTransformer
from config import CHROMA_PERSIST_PATH, CHROMA_COLLECTION_NAME, DOCUMENTS_PATH, EMBEDDING_MODEL_NAME

class ChromaIndexBuilder:
    def __init__(self, data_path=DOCUMENTS_PATH,
                 collection_name=CHROMA_COLLECTION_NAME,
                 model_name=EMBEDDING_MODEL_NAME,
                 persist_dir=CHROMA_PERSIST_PATH):
        self.data_path = data_path
        self.model_name = model_name
        self.persist_dir = persist_dir
        self.collection_name = collection_name

        os.makedirs(self.persist_dir, exist_ok=True)
        self.client = client
        self.model = SentenceTransformer(self.model_name)
        self.collection = None
        self.documents = []

    def load_documents(self):
        with open(self.data_path, "r") as f:
            self.documents = json.load(f)
        print(f"Loaded {len(self.documents)} documents")

    def prepare_collection(self):
        #if self.collection_name in [c.name for c in self.client.list_collections()]:
        #    self.client.delete_collection(self.collection_name)

        self.collection = self.client.create_collection(name=self.collection_name)
        print(f"Created Chroma collection: {self.collection_name}")

    def embed_and_store(self):
        if not self.documents:
            raise ValueError("Documents not loaded")

        embeddings = self.model.encode(self.documents, convert_to_numpy=True)
        ids = [f"doc_{i}" for i in range(len(self.documents))]

        try:
            self.collection.add(
                documents=self.documents,
                embeddings=embeddings,
                ids=ids
            )
            print(f"Stored {len(self.documents)} embeddings in Chroma")
            print("Collection count:", self.collection.count())

            results = self.collection.get(include=["documents", "metadatas"])
            for i, doc in enumerate(results["documents"]):
                print(f"{results['ids'][i]} ➜ {doc[:80]}...")

        except Exception as e:
            print("Failed to store in Chroma:", e)

    def persist(self):
        self.client.persist()
        print(f"Chroma index persisted at {self.persist_dir}")

    def run(self):
        self.load_documents()
        self.prepare_collection()
        self.embed_and_store()
