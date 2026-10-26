from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

res = client.chat.completions.create(
    model=os.getenv("MODEL_NAME"),
    messages=[
        {
        "role" : "user",
        "content" : "Hello ! "
        }
    ]
)

# while True:
#     user_input = input("Yout" + " input : ")


print("Ollam response : ")
print(res.choices[0].message.content)
