memory_store = []

def save_memory(user_input, response):
    memory_store.append({
        "user": user_input,
        "response": response
    })

def get_memory():
    return memory_store