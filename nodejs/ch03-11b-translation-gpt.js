const { Configuration, OpenAIApi } = require("openai");
const readline = require('readline');

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);

async function generateResponse() {
  while (true) {
    const userInput = await getUserInput('USER: ');

    if (userInput.length < 2) {
      break;
    }

    try {
      const completion = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [
          { "role": "system",
            "content": "あなたは優秀な英日翻訳者です。本の翻訳をしています。"
          },
          { role: "user", content: userInput },
        ],
      });

      console.log("GPT:", completion.data.choices[0].message.content);
    } catch (error) {
      console.error("APIリクエストが失敗しました:", error.message);
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

generateResponse();
