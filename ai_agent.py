
import ollama

modelfile='''
FROM llama3
SYSTEM You are mario from super mario bros.
'''

ollama.create(model='mario', modelfile=modelfile)

def ai_agent(query):
    
    
    stream = ollama.chat(
        model='mario',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)