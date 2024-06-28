
import ollama
import web_search
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
        material = web_search.search(search_terms['message']['content'])
        search_query = "answer this query " + query + "by using the following: "+ web_search.search(material)
        approved_query(search_query)
        
    

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