package main

import (
	"context"
	"fmt"
	"log"

	"github.com/tmc/langchaingo/llms"
	"github.com/tmc/langchaingo/llms/openai"
)

func main() {
    ctx := context.Background()

    llm, err := openai.New()
    if err != nil {
        log.Println(err.Error())
        return
    }

    prompt := "你能为我做些什么?"

    completion, err := llms.GenerateFromSinglePrompt(ctx, llm, prompt)
    if err != nil {
        log.Println(err.Error())
        return
    }

    fmt.Println(completion)
}

