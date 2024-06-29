import ai_agent
import model

def main():
    """
    Main function to run the AI agent interaction loop.
    """
    
    model.create_models()
    
    while True:
        print("")
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        ai_agent.handle_message(user_input)

if __name__ == "__main__":
    main()