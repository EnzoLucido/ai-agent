
import ollama

def ai_agent(query):

    classification = ollama.chat(
        model='classifier',
        messages=[{'role':'user', 'content': query}]
    )
    
    if classification['message']['content'] == "B":
        approved_query(query)
    else:
        search_terms = ollama.chat(
            model='search_term_creator',
            messages=[{'role':'user', 'content':query}]
        )
        
        print(search_terms['message']['content'])
    

def approved_query(query):
    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        
    # Join the response chunks into a single string

    
    # Check if the first words are "surfing the web"