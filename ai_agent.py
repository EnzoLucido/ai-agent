
import ollama

def ai_agent(query):

    classification = ollama.chat(
        model='classifier',
        messages=[{'role':'user', 'content': query}]
    )
    
    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': cleared_query}],
        stream=True,
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        
    # Join the response chunks into a single string

    
    # Check if the first words are "surfing the web"