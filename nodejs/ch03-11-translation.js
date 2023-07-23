const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

const readline = require('readline');  // userからの入力を読み込む
generateResponse();

async function generateResponse() {
  while (true) {
    const userInput = await getUserInput('USER: ');

    if (! userInput) {
      break;
    }

    const completion = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [
        {"role": "system", "content": "あなたは優秀な英日翻訳者です。本の翻訳をしています。"},
        {role: "user", content: userInput}],
    });
  
    console.log("GPT:", completion.data.choices[0].message.content);
  }
}


// プロンプトを読み込む
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
