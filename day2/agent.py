import re
from tools import calculator, weather, summarize_text
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ToolAgent:

    def identify_intent(self, user_input):
        if "calculate" in user_input or any(op in user_input for op in ["+", "-", "*", "/"]):
            return "calculator"
        elif "weather" in user_input:
            return "weather"
        elif "summarize" in user_input or "summary" in user_input:
            return "summarize"
        else:
            return "llm_fallback"

    def handle_query(self, user_input):
        intent = self.identify_intent(user_input)
        if intent == "calculator":
            expression = user_input.replace("calculate", "").strip()
            return calculator(expression)
        elif intent == "weather":
            words = user_input.split()
            city = words[-1]
            return weather(city)
        elif intent == "summarize":
            text = user_input.replace("summarize", "").strip()
            return summarize_text(text)
        else:
            return self.ask_llm(user_input)

    def ask_llm(self, query):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message.content