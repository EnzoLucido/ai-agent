
import ollama
from datetime import datetime

date_and_time = datetime.now()
date = date_and_time.strftime("%B %d, %Y")
instruction = f'If the user asks you for information about something that has happened on or after December 29th, 2022 immediately reply "searching the web" and then summarize the users query into a search phrase. Otherwise, you can respond normally. You know that the date is {date}, which is after December 29th,2022. Do not know anything else about what has happened since December 29th, 2022'

modelfile=f'''
FROM llama3
SYSTEM {instruction}
'''

ollama.create(model='mario', modelfile=modelfile)

def ai_agent(query):
    stream = ollama.chat(
        model='mario',
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    print("AI: ")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)