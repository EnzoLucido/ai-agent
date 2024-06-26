# ai_agent.py

from transformers import LLaMATokenizer, LLaMAForCausalLM

tokenizer = LLaMATokenizer.from_pretrained('path/to/llama-3')
model = LLaMAForCausalLM.from_pretrained('path/to/llama-3')

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0])

def ai_agent(query):
    if 'search the web for' in query.lower():
        from web_search import search_web
        search_query = query.split('search the web for')[-1].strip()
        return search_web(search_query)
    else:
        return generate_response(query)
