# main.py

import ai_agent

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = ai_agent.test(user_input)
        print(f"AI: {response}")
