from openai import OpenAI
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="YOUR_API_KEY"
)

res = client.chat.completions.create(
    model="qwen:4b",
    messages=[
        {
        "role" : "user",
        "content" : "Hello ! "
        }
    ]
)

print("Ollam response : ")
print(res.choices[0].message.content)
