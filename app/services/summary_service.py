conversation_summary =  (
   "User name is Vaibhav"
)

def save_summary(text):
    global conversation_summary
    conversation_summary = text
    
def get_summary():
    return conversation_summary

def clear_summary():
    global conversation_summary
    conversation_summary = ""