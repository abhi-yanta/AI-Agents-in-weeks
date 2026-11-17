import sys
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL = "gemini-3.5-flash-lite"


def ask_gemini(question):
    client = genai.Client()

    start_time = time.perf_counter()

    response = client.models.generate_content(
    model=MODEL,
    contents=question,
    config=types.GenerateContentConfig(
        temperature=0.2
    )
)

    elapsed = time.perf_counter() - start_time

    print("\nGemini:", response.text)
    print(f"\nTime taken: {elapsed:.2f} seconds")

    usage = response.usage_metadata

    if usage:
        print(f"Input tokens: {usage.prompt_token_count}")
        print(f"Output tokens: {usage.candidates_token_count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: uv run python week2/ask.py "Your question"')
    else:
        question = " ".join(sys.argv[1:])
        ask_gemini(question)

    
    
