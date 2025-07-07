# app.py
from modules.database import DatabaseManager
from modules.embedding import ChromaIndexBuilder
from modules.query_retriever import QueryRetriever
from modules.prompt_builder import PromptBuilder

class App:
    def __init__(self):
        self.db = DatabaseManager()
        self.indexer = ChromaIndexBuilder()
        self.indexer.run()
        self.retriever = QueryRetriever()
        self.prompter = PromptBuilder()

    def run_retrieval(self):
        question = input("\nAsk a question about the transaction system: ")
        top_chunks = self.retriever.retrieve(question, top_k=3)
        prompt = self.prompter.build(question, top_chunks)
        return prompt

    def run(self):
        # Step 1: Initialize DB
        print("Initializing database...")
        self.db.initialize_db()

        # Step 2: Run sample query
        print("Running test query...")
        rows = self.db.execute_query("SELECT * FROM transactions;")
        for row in rows:
            print(row)

        print("Embedding documents and building chroma DB...")
        context_chunks = self.run_retrieval()

        print("All setup steps complete.")
        self.db.close()

if __name__ == "__main__":
    app = App()
    app.run()

