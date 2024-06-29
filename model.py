import ollama
from datetime import datetime

def create_models():
    classifier()
    search_term_creator()
    


def classifier():
    
    '''
        Classifies whether or not we need to search for answers
        Responds "A" for yes, "B" for no
        These unintuitive variables seem to encourage AI to make a clean pick
    '''

    date_and_time = datetime.now()
    date = date_and_time.strftime("%B %d, %Y")
    date_instruction = f'You know that the date is {date},' 
    date_instruction = ' which is after December 29th,2022. You do not know anything else about what has happened since December 29th, 2022. If the user asks for a story from today or a period of time ago, you should respond with A.' 

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
    
def verifier():
    '''
        Verifies that we have found the right information
        Currently unused.
    '''
    with open('instructions/verifier.txt', 'r') as file:
        # Read the entire content of the file
        instruction = file.read()

    modelfile=f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='verifier', modelfile=modelfile)
    
def added_info():
    '''
        Handles queries where there has been info 
        added from the internet
    '''
    with open('instructions/added_info.txt', 'r') as file:
        # Read the entire content of the file
        instruction = file.read()

    modelfile=f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='added_info', modelfile=modelfile)
    
