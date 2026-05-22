from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv
from app.services.prompt_service import SYSTEM_PROMPT
from app.config import settings

# client = OpenAI(
#     api_key=settings.OPEN_API_KEY
# )
genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

# def ask_ai(question: str):
#     response = client.chat.completions.create(
#         model='gpt-4o',
#         messages = [
#                 {"role": "system", "content": SYSTEM_PROMPT},
#                 {"role": "user", "content": question}
#                 ]
#                 )
#     return  response.choices[0].message.content

def ask_ai(question: str):

    try:

        full_prompt = f"""
        {SYSTEM_PROMPT}

        User:
        {question}
        """

        response = model.generate_content(
            full_prompt
        )

        return response.text

    except Exception as e:

        return str(e)

