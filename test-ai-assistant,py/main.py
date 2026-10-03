from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

question = input("Ask me something: ")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=question
)

print("\nAI:", response.text)