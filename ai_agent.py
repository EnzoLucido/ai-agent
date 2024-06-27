
import ollama

def ai_agent(query):
    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)