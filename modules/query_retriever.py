import chromadb
from modules.chroma_client import client
from sentence_transformers import SentenceTransformer
import os

class QueryRetriever:
    def __init__(self,
                 collection_name="schema_docs",
                 model_name="all-MiniLM-L6-v2",
                 persist_dir="embeddings/chroma"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        persist_path = os.path.join(base_dir, persist_dir)

        self.client = client
        self.model = SentenceTransformer(model_name)
        self.collection = self.client.get_collection(collection_name)

    def retrieve(self, user_query: str, top_k=3):
        print(f"Retrieving for query: {user_query}")
        embedding_vector = self.model.encode(user_query, convert_to_numpy=True)
        query_embedding = [embedding_vector.tolist()]

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k,
            include=["documents"]
        )

        documents = results["documents"][0]
        print(f"Top {top_k} documents retrieved:")
        for i, doc in enumerate(documents):
            print(f"{i+1}. {doc[:80]}...")

        return documents

