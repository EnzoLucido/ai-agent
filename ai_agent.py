
import ollama
import model

def ai_agent(query):
    model.surfing_llama()
    
    stream = ollama.chat(
        model='surfing_llama',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    print("AI: ")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)