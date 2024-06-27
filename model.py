import ollama
from datetime import datetime

def surfing_llama():

    date_and_time = datetime.now()
    date = date_and_time.strftime("%B %d, %Y")
    date_instruction = f'You know that the date is {date}, which is after December 29th,2022. You do not know anything else about what has happened since December 29th, 2022'

    with open('instruction.txt', 'r') as file:
        # Read the entire content of the file
        file_content = file.read()
        
    instruction = file_content + date_instruction

    modelfile=f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    print(instruction)
    ollama.create(model='surfing_llama', modelfile=modelfile)