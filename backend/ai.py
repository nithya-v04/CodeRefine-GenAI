import time
from google import genai

client = genai.Client(api_key="")

def review_code(code):

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

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-pro-latest",  # more stable than flash
                contents=prompt,
            )
            return response.text
        except Exception as e:
            print("Gemini error, retrying...", e)
            time.sleep(2)

    return "Gemini unavailable due to high demand."
