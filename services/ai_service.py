import os
import time
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


def ask_ai(prompt: str):

    retries = 3

    for attempt in range(retries):

        try:
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:

            error_message = str(e)

            if "429" in error_message:

                time.sleep(20)

            else:
                return f"Error: {error_message}"

    return "Rate limit exceeded. Please try again later."