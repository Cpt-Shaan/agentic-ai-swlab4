import re
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_numbers(text):
    numbers = re.findall(r'\d+', text)
    numbers = [int(n) for n in numbers]
    return numbers

def compute_average(numbers):
    if len(numbers) == 0:
        return None
    avg = sum(numbers) / len(numbers)
    return avg

def summarize_result(result):
    prompt = f"""
    Write a short one sentence summary of the following result.

    Result:
    {result}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content