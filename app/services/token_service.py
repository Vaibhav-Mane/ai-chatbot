import tiktoken 

def estimate_token(messages):
    encoding = tiktoken.get_encoding("cl100k_base")
    
    total = 0
    for m in messages:
        tokens  = encoding.encode(m["content"])    
        total += len(tokens)
        
    return total