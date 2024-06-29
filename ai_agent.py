
import ollama
import web_search
import re


def handle_message(query):
    classification = ollama.chat(
        model='classifier',
        messages=[{'role':'user', 'content': query}]
    )
    
    if classification['message']['content'] == "A":
        
        print("AI: Please wait while I am searching web")
        
        search_terms = ollama.chat(
            model='search_term_creator',
            messages=[{'role':'user', 'content':query}]
        )
        search_terms = sanitize_search_term(search_terms['message']['content'])
        print(search_terms)
        material = web_search.search(search_terms)
        query = "answer this query " + query + "by using the following: "+ web_search.search(material) + "Do not mention that you were provided snippets"
    
    approved_query(query)
        
    

def approved_query(query):
    
    
    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )
    
    print("AI: ", end='', flush=True)
    
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        
        
def sanitize_search_term(search_term):
    # Remove special characters
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', search_term)
    return sanitized       