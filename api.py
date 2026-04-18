from google import genai
from dotenv import load_dotenv
import os

load_dotenv(".env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# generate summary
def generate_summary(notes,language):
    prompt = f"Summarize this notes in a interesting way under 200 words and use Language: {language}. Give a markdown response with proper heading, highlighting and listing.",
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[prompt,notes]
    )
    return response.text

# generate quiz
def generate_quiz(notes,language,difficulty_level):
    prompt = f"Generate a quiz (Multiple Choice Questions) based on these notes with no answer. Use Language: {language} and Difficulty Level: {difficulty_level}. Give a markdown response with proper heading, highlighting and listing.",
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[prompt,notes]
    )
    return response.text

def check_answer(quiz):
    prompt = f"can you analyze this {quiz}, and check is answes are correct or not. give a markdown response with proper heading, highlighting and listing."
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[prompt]
    )
    return response.text
