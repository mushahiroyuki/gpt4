import os
import openai

def read_user_input(): ## ユーザーから入力を受け取る関数
    user_input = input("原文: ")
    if user_input == "":
        return ""

    while True:
        new_input = input("")
        if new_input == "":
            return user_input
        else:
            user_input += "\n" + new_input

## 本体部分
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = read_user_input()
    if user_input == "":
        break
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "あなたは優秀な英日翻訳者です。本の翻訳をしています。",
            },
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
    print("訳文:", response["choices"][0]["message"]["content"])
    print()
