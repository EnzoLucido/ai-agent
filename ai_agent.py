
import ollama

def ai_agent(query):
    
    response = []
    
    stream = ollama.chat(
        model='surfing_llama',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    print("AI: ")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        response.append(chunk['message']['content'])
    
    # Join the response chunks into a single string
    full_response = ''.join(response)
    
    # Check if the first words are "surfing the web"
    if full_response.lower().startswith("surfing the web"):
        print("The response starts with 'surfing the web'.")
    else:
        print("The response does not start with 'surfing the web'.")