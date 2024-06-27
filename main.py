# main.pyelse to the search

import ai_agent
import model

if __name__ == "__main__":
    
    model.classifier()
    model.search_term_creator()
    
    while True:
        print("")
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = ai_agent.ai_agent(user_input)
        #print(f"AI: {response}")
