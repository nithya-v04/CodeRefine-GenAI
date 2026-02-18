import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code_groq(code):

    prompt = f"""
You are a senior software engineer.

Review this GitHub Pull Request diff.

Bugs:
Performance:
Security:
Best Practices:

Code:
{code}
"""

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content
