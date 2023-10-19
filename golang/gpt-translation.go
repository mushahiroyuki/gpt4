package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"os"
	"bufio"
	openai "github.com/sashabaranov/go-openai"
)

func main() {
	key := os.Getenv("OPENAI_API_KEY")  // 環境変数からAPIキーを取得
	c := openai.NewClient(key) 
	ctx := context.Background() // contextを初期化。キャンセル等の処理のため

	for {
		userInput := getUserInput("原文: ")

		if len(userInput) < 3 {
			break
		}
		
		req := openai.ChatCompletionRequest{
			Model:     openai.GPT3Dot5Turbo,
			MaxTokens: 300,
			Messages: []openai.ChatCompletionMessage{
				{
					Role: "system",
					Content: "あなたは優秀な英日翻訳者です。本の翻訳をしています。",
				},
				{
					Role:   "user",
					Content: userInput,
				},
			},
			Stream: true,
		}
		stream, err := c.CreateChatCompletionStream(ctx, req)
		if err != nil {
			fmt.Printf("ChatCompletionStream error: %v\n", err)
			return
		}

		defer stream.Close()

		fmt.Printf("訳文: ")
		for {
			response, err := stream.Recv()
			if errors.Is(err, io.EOF) {
				fmt.Println("\n")
				break
			}
			
			if err != nil {
				fmt.Printf("\nStream error: %v\n", err)
				return
			}
			
			fmt.Printf(response.Choices[0].Delta.Content)
		}
	}
}


func getUserInput(prompt string) string {
	fmt.Print(prompt)
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	return input
}
