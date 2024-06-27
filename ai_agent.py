
import ollama

modelfile='''
FROM llama3
SYSTEM If the user asks you for information about something that has happened on or after January 1st, 2023 reply "searching the web" and then summarize the user's query into a short search phrase. You may assume that today is in May 2024. 
".
'''

ollama.create(model='mario', modelfile=modelfile)

def ai_agent(query):
    
    
    stream = ollama.chat(
        model='mario',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    print("AI: ")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)