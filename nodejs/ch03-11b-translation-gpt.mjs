import OpenAI from "openai";
import readline from "readline";

const API_KEY = process.env.OPENAI_API_KEY;
if (!API_KEY) {
  console.error('APIキーが設定されていません。');
  process.exit(1);
}

const openai = new OpenAI({ apiKey: API_KEY });
generateResponse();

async function generateResponse() {
  while (true) {
    const userInput = await getUserInput('原文: ');

    if (! userInput) {
      break;
    }

    try {
      const completion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [
          {
            "role": "system",
            "content": "あなたは優秀な英日翻訳者です。本の翻訳をしています。"
          },
          {
            "role": "user",
            "content": userInput
          },
        ],
        temperature: 1,
        max_tokens: 256,
        top_p: 1,
        frequency_penalty: 0,
        presence_penalty: 0,
      });
      console.log("訳文:", completion.choices[0].message.content);
    } catch (error) {
      console.error('APIからのレスポンスにエラーがありました:', error.message);
    }
  }
}

function getUserInput(prompt) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve) => {
    rl.question(prompt, (input) => {
      rl.close();
      resolve(input);
    });
  });
}
