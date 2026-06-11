import os
import google.generativeai as genai

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def ask_ai(prompt: str):

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"