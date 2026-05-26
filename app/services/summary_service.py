from ollama import chat

conversation_summary = ""

def genrate_summary(messages):
    global conversation_summary
    try:
        text = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        response = chat(
            model="llama3.2", 
            messages=[{
            "role":"system",
            "content":
            "Summarize this conversation in short"
            },
            {
                "role":"user",
                "content":text
            }
            ]
        )
        conversation_summary = (
            response["message"]["content"]
        )
        print("\n===== SUMMARY CREATED =====")
        print(conversation_summary)
        print("===========================\n")
    except Exception as e:
        print(e)   
         

def get_summary():
    return conversation_summary

def clear_summary():
    global conversation_summary
    conversation_summary = ""