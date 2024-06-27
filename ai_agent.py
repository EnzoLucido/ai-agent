
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0])

def test(user_input):
    # Example response generation logic
    return f"Echo: {user_input}"

def ai_agent(query):
    if 'search the web for' in query.lower():
        from web_search import search_web
        search_query = query.split('search the web for')[-1].strip()
        return search_web(search_query)
    else:
        return generate_response(query)
