import os
import openai

def read_user_input():  ## ユーザーから入力を受け取る関数
    user_input = input("USER: ")
    if user_input == "": ## 空行が入力されたら空文字列を返す
        return ""

    while True:  ## 2つ目以降のパラグラフの処理
        new_input = input("")
        if new_input == "":  ## 空行が入力されたらここまでの入力を戻す
            return user_input
        else:
            user_input += "\n" + new_input  ## 後ろに追加

## 本体部分
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:  ## 無限ループ
    user_input = read_user_input()
    if user_input == "":  ## 空行が入力されたら終了
        break
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
    print()   ## 区切りの空行を出力
