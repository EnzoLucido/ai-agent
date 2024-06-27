
import ollama

def ai_agent(query):
    response = ollama.chat(model='llama3', messages=[
    { 
        'role': 'user',
        'content': query,
    },
    ])
    #print(response['message']['content'])
    return response['message']['content']