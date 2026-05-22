from openai import OpenAI
from ollama import chat
import google.generativeai as genai
from dotenv import load_dotenv
from app.services.prompt_service import SYSTEM_PROMPT
from app.config import settings
from app.services.memory_service import add_message, get_message

# client = OpenAI(
#     api_key=settings.OPEN_API_KEY
# )
genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)
##########################for openai###############################
# def ask_ai(question: str):
#     response = client.chat.completions.create(
#         model='gpt-4o',
#         messages = [
#                 {"role": "system", "content": SYSTEM_PROMPT},
#                 {"role": "user", "content": question}
#                 ]
#                 )
#     return  response.choices[0].message.content


##################### for ollama ###########################
def ask_ai(question: str):

    try:
        add_message("user", question)
        
        messages = [
            {
            "role": "system",
            "content": SYSTEM_PROMPT
            }
        ]
        
        messages.extend(
            get_message())
        
        respopnse = chat(
            model= "llama3.2",
            messages = messages)
        
        ai_reply = respopnse["message"]["content"]
        add_message("assistant", ai_reply)

        return {
                "success": True,
                "data": ai_reply
                }        

    except Exception as e:

        return {
                "success": False,
                "error":str(e)
                }

