import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY") # 環境変数からAPIのキーを取得

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "情報の正確性という観点から次のツイートを分析してください。\nツイート: 50%以上の科学者は気候変動を信じていない。"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["message"]["content"])
