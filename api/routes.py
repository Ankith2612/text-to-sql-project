from flask import Blueprint, request, jsonify
from modules.database import DatabaseManager
from modules.embedding import ChromaIndexBuilder
from modules.query_retriever import QueryRetriever
from modules.prompt_builder import PromptBuilder
from modules.mistral_llm import MistralLLM

main = Blueprint("main", __name__)

# Load components once on startup
db = DatabaseManager()
chroma = ChromaIndexBuilder().run()
retriever = QueryRetriever()
prompter = PromptBuilder()
llm = MistralLLM()

# api/routes.py

@main.route("/", methods=["GET"])
def index():
    print("✅ / route was hit")
    return "<h2>✅ Mistral SQL API is running!</h2>", 200

@main.route("/query", methods=["POST"])
def handle_query():
    data = request.get_json()
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # retrieve context
        chunks = retriever.retrieve(user_question)
        prompt = prompter.build(user_question, chunks)
        sql = llm.generate_sql(prompt)

        # run SQL
        results = db.execute_query(sql)

        return jsonify({
            "question": user_question,
            "sql": sql,
            "results": results
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
