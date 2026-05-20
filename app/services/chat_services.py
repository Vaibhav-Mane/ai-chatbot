def get_reply(message:str):
    
    msg= message.lower()
    
    if "hello" in msg:
        return "Hello! How can I assist you today?"
    elif "how are you" in msg:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "fastapi" in msg:
        return "FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints."
    elif "bye" in msg:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"
    