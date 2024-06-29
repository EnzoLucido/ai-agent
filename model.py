import ollama
import web_search


def create_models():
    classifier()
    search_term_creator()
    


def classifier():
    
    '''
        Classifies whether or not we need to search for answers
        Responds "A" for yes, "B" for no
        These unintuitive variables seem to encourage AI to make a clean pick
    '''

    date_instruction = web_search.date() + ' which is after December 29th,2022. You do not know anything else about what has happened since December 29th, 2022. If the user asks for a story from today or a period of time ago, you should respond with A.' 

    with open('instructions/classifier.txt', 'r') as file:
        # Read the entire content of the file
        instruction = file.read()
        
    instruction = instruction + date_instruction

    modelfile=f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='classifier', modelfile=modelfile)
    
def search_term_creator():
    '''
        Creates search terms to be fed into webscraper
    '''
    
    with open('instructions/search_terms.txt', 'r') as file:
        # Read the entire content of the file
        instruction = file.read()

    modelfile=f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='search_term_creator', modelfile=modelfile)