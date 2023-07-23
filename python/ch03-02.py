import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


user_input = input("USER: ")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
    temperature=1,
    max_tokens=2560,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print("GPT:", response["choices"][0]["message"]["content"])
