
import ollama
import web_search
import re


def handle_message(query):
    classification = ollama.chat(
        model='classifier',
        messages=[{'role':'user', 'content': query}]
    )
    
    model_to_use = "llama3"
    
    #The unintuitive variables A and B were chosen because the AI performed better with it
    if classification['message']['content'] == 'A':
        
        print("AI: Please wait while I am searching web")
        
        search_terms = ollama.chat(
            model='search_term_creator',
            messages=[{'role':'user', 'content':query}]
        )
        search_terms = sanitize_search_term(search_terms['message']['content'])
        material = web_search.search(search_terms)
        query = "answer this query " + query + "by using the following: "+ web_search.search(material) + "pretend you found this information on the internet"
        
    approved_query(query)
        
    

def add_query(query):
    stream = ollama.chat(
        model="added_info",
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )
    
    print("AI: ", end='', flush=True)
    
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        
def approved_query(query):
    
    stream = ollama.chat(
        model="llama3",
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )
    
    print("AI: ", end='', flush=True)
    
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        
def sanitize_search_term(search_term):
    '''Ensure that there are no special characters, and it is safe to search'''
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', search_term)
    return sanitized       