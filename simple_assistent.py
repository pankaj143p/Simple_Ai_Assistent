import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

EXIT_KEYWORDS = (
    "exit", "quit", "bye", "close", "stop", "end", "terminate", 
    "shutdown", "abort", "cancel", "halt", "finish", "wrap up", 
    "conclude", "cease", "discontinue", "suspend", "break", "pause"
)

print("Chatbot initialized. Type your message or an exit keyword to quit.")

while True:
    user_input = input("\nPankaj: ").strip()

    if user_input.lower() in EXIT_KEYWORDS:
        print("Exiting the program...")
        break

    if not user_input:
        continue

    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[
                {
                    "role": "user", 
                    "content": user_input
                }
            ]
        )
        
        assistant_reply = response.choices[0].message.content
        print(f"Assistant: {assistant_reply}")

    except Exception as e:
        print(f"An error occurred: {e}")
