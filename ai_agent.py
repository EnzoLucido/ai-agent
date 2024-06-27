
import ollama

def ai_agent(query):
    
    stream = ollama.chat(
        model='surfing_llama',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    print("AI: ")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)