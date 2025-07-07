# modules/mistral_llm.py
import requests
from config import OLLAMA_BASE_URL, LLM_MODEL

class MistralLLM:
    def __init__(self):
        self.model = LLM_MODEL
        self.api_url = f"{OLLAMA_BASE_URL}/api/generate"

    def generate_sql(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            print("Sending prompt to Mistral via Ollama...")
            response = requests.post(self.api_url, json=payload)

            if response.status_code != 200:
                raise Exception(f"Failed: {response.status_code} - {response.text}")

            data = response.json()
            generated_text = data.get("response", "").strip()

            print("SQL received from LLM:")
            print(generated_text)
            return generated_text

        except Exception as e:
            raise RuntimeError(f"Error generating SQL with Mistral: {str(e)}")
