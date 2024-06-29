
import ollama
import web_search


def handle_message(query):
    """
    Handles the user's query by deciding if it should search the internet or not 
    
    If yes, it creates seach terms, incorporates the newly found information into it's answer. 
    
    Otherwise, it runs normally
    
    Args:
        query (str): The user's query.
    """
    
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
        search_terms = web_search.sanitize_search_term(search_terms['message']['content'])
        material = web_search.search(search_terms)
        query = "answer this query " + query + "by using the following: "+ web_search.search(material) + "pretend you found this information on the internet" + web_search.date()
        
    approved_query(query)
        
        
def approved_query(query):
    
    stream = ollama.chat(
        model="llama3",
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )
    
    print("AI: ", end='', flush=True)
    
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        
      