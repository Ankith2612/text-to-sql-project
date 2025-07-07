class PromptBuilder:
    def __init__(self):
        self.template = (
            "You are an expert data analyst. You have access to the following database schema and information:\n\n"
            "{context}\n\n"
            "Based on this, write an accurate and executable SQL query for the following question:\n\n"
            "Question: {question}\n\n"
            "Only return the SQL query."
        )

    def build(self, question: str, context_chunks: list[str]) -> str:
        context_text = "\n\n".join(context_chunks)
        prompt = self.template.format(context=context_text, question=question)
        print("\n Prompt built for LLM:")
        print("=" * 80)
        print(prompt)
        print("=" * 80)
        return prompt

