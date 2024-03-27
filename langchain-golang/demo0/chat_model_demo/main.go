package main

import (
	"context"
	"fmt"
	"log"

	"github.com/tmc/langchaingo/llms"
	"github.com/tmc/langchaingo/llms/openai"
	"github.com/tmc/langchaingo/schema"
)

func main() {
    llm, err := openai.New()
    if err != nil {
        log.Println(err.Error())
        return
    }

    ctx := context.Background()

    messages := []llms.MessageContent{
        llms.TextParts(schema.ChatMessageTypeSystem, "你是一个Go语言开发工程师"),
        llms.TextParts(schema.ChatMessageTypeHuman, "帮我用gin框架写一个简单的http服务器demo"),
    }

    completion, err := llm.GenerateContent(ctx, messages, llms.WithStreamingFunc(func(ctx context.Context, chunk []byte) error {
        fmt.Println(string(chunk))
        return nil
    }))

    if err != nil {
        log.Println(err.Error())
        return
    }

    fmt.Println(completion)
}
