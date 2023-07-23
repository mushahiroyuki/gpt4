import os
import openai

def read_user_input():  ## ユーザーから入力を受け取る関数
    user_input = input("USER: ")
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
history = []  ## 履歴（history）を記憶しておくリスト

while True:   ## 無限ループ
    user_input = read_user_input()
    if user_input == "":  ## 空行が入力されたら終了
        break
    history.append({   ## プロンプトをリストの最後に追加
        "role": "user",
        "content": user_input
    })
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history,
        temperature=1,
        max_tokens=2560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print("GPT:", response["choices"][0]["message"]["content"]) ## 結果の表示
    print("")
    history.append(response["choices"][0]["message"]) ##コンプリーションを履歴に追加

## 途中経過を見る場合    
##    print("===========")
##    for i, element in enumerate(history):
##        print(f"{i}: {element['role']} -- {element['content']}")
