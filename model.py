import ollama
from datetime import datetime

def classifier():

    date_and_time = datetime.now()
    date = date_and_time.strftime("%B %d, %Y")
    date_instruction = f'You know that the date is {date}, which is after December 29th,2022. You do not know anything else about what has happened since December 29th, 2022. If the user asks for a story from today or a period of time ago, you should respond with A.' 

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
    with open('instructions/search_terms.txt', 'r') as file:
        # Read the entire content of the file
        instruction = file.read()

    modelfile=f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='search_term_creator', modelfile=modelfile)