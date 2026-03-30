import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_plan(query):
    prompt = f"""
    You are a planning agent.
    Break the user task into sequential steps.

    Available tools:
    - extract_numbers
    - compute_average
    - summarize_result

    Respond ONLY with the steps as a numbered list.

    Example:
    1. extract_numbers
    2. compute_average
    3. summarize_result

    Query:
    {query}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    plan_text = response.choices[0].message.content
    steps = []
    for line in plan_text.split("\n"):
        if "." in line:
            step = line.split(".", 1)[1].strip()
            steps.append(step)
    return steps