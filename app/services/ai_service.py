from openai import OpenAI
from ollama import chat
# import google.generativeai as genai
from dotenv import load_dotenv
from app.services.prompt_service import SYSTEM_PROMPT
from app.config import settings
from app.services.memory_service import add_message, get_message
from app.services.summary_service import get_summary
from app.services.summary_service import genrate_summary
from app.services.token_service import estimate_token                                                                                                                                                                                                                                                                                                             

# client = OpenAI(
#     api_key=settings.OPEN_API_KEY
# )
# genai.configure(api_key=settings.GEMINI_API_KEY)

# model = genai.GenerativeModel(
#     "gemini-2.0-flash"
# )
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
def ask_ai(user_id: str, question: str, background_tasks):

    try:
        add_message(user_id, "user", question)
        history = get_message(
            user_id
        )

        if len(history) >= 5:
            background_tasks.add_task(genrate_summary, history)
        
        messages = [

            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role":"system",
                "content":
                f"Conversation summary: {get_summary()}"
            }

        ]
        
        messages.extend(history)
        
        estimated_tokens = estimate_token(messages)
        print(f"Estimated tokens: {estimated_tokens}")
        
        messages.extend(history)

        estimated_tokens = estimate_token(messages)

        print(
            f"Estimated tokens: {estimated_tokens}"
        )
        
        if estimated_tokens > 300:
            messages = messages[-10:]
            print("trimmed context")
        
        respopnse = chat(
            model= "llama3.2",
            messages = messages)
        
        ai_reply = respopnse["message"]["content"]
        add_message(user_id, "assistant", ai_reply)

        return {
                "success": True,
                "data": ai_reply
                }        

    except Exception as e:

        return {
                "success": False,
                "error":str(e)
                }

