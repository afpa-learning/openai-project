from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

client = OpenAI(
  api_key=openai_api_key
)

response = client.responses.create(
  model="gpt-5-nano",
  input="Bonjour, ChatGPT !",
  store=True,
)

print(response.output_text);
