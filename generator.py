import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads GEMINI_API_KEY from .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_with_gemini(context_text, image_urls, user_query):
    prompt = f"""
You are a helpful assistant. Based on the content retrieved from a website, generate a structured, clear, and detailed documentation-style response to the user query.

--- WEBSITE TEXT ---
{context_text}

--- IMAGES IN PAGE ---
{', '.join(image_urls)}

--- USER QUERY ---
{user_query}

Format the answer with headings and clarity. Include image descriptions where relevant.
"""
    response = model.generate_content(prompt)
    return response.text
