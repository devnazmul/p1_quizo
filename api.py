import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv(".env")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")



def generate_summary(notes, language):
    prompt = f"""
    Summarize these notes in an interesting way under 200 words.
    Language: {language}.
    Use markdown with headings, highlights, and lists.

    Notes:
    {notes}
    """
    response = model.generate_content(prompt)
    return response.text

def generate_quiz(notes, language, difficulty_level):
    prompt = f"""
    Generate a quiz (Multiple Choice Questions) from these notes WITHOUT answers.
    Language: {language}
    Difficulty: {difficulty_level}
    Format: markdown with headings and lists.

    Notes:
    {notes}
    """
    response = model.generate_content(prompt)
    return response.text

def check_answer(quiz):
    prompt = f"""
    Analyze this quiz and check whether the answers are correct.
    Return markdown with clear sections.

    Quiz:
    {quiz}
    """
    response = model.generate_content(prompt)
    return response.text