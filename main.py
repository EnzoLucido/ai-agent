import ai_agent
import model

def main():
    """
    Main function to run the AI agent interaction loop.
    """
    
    model.classifier()
    model.search_term_creator()
    
    while True:
        print("")
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = ai_agent.handle_message(user_input)

if __name__ == "__main__":
    main()