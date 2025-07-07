# 🧠 Text-to-SQL Chatbot App

A full-stack, production-ready application that translates **natural language questions into executable SQL queries** using **Mistral 7B LLM**, **ChromaDB** for context retrieval, and a real-time **SQLite** backend.

---

## 🏗️ Features

- 🔎 Natural Language → SQL Conversion
- 🧠 Mistral 7B (via Ollama) for LLM inference
- 🔁 ChromaDB for schema/contextual retrieval (RAG)
- 💡 Real-time SQL execution & result display
- 🧩 Feedback mechanism for user rating (👍 / 👎)
- 🌐 Frontend built with React + Flask API backend
- 🐳 Docker-ready design

---

## 🧱 Tech Stack
--------------------------------------------
| Layer        | Tool                      |
|--------------|---------------------------|
| LLM          | Mistral 7B via Ollama     |
| Vector DB    | ChromaDB                  |
| Embeddings   | sentence-transformers     |
| Backend API  | Flask                     |
| Frontend     | React                     |
| DB Engine    | SQLite                    |
| Dev Support  | Docker, virtualenv, curl  |
--------------------------------------------

## 📐 Architecture



# 📦 Setup on macOS with pyenv
brew install pyenv

# Install a Python version compatible with ChromaDB
pyenv install 3.11.9

# Set local Python version for the project
cd nl2sql_project/
pyenv local 3.11.9

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install project dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the backend app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start Ollama and load Mistral model
ollama run mistral

# Run the backend API
python -m api.server.py

# Run the Frontend App
cd frontend/

npm install

npm start

# Sample Prompt
Use the following schema and examples to answer the question:
Schema:
- Table: transactions (id, amount, network, status)
Question: Show all Mastercard payments over $200



