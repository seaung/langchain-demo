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

    /*
    New方法可以接受返回Optionl类型的参数,类似与WithXXX的方法参数
    */
    llm, err := openai.New()
    if err != nil {
        log.Println(err.Error())
        return
    }

    prompt := "你能为我做些什么?"

    // GenerateFromSinglePrompt用于简单的字符串输入和响应的操作
    completion, err := llms.GenerateFromSinglePrompt(ctx, llm, prompt)
    if err != nil {
        log.Println(err.Error())
        return
    }

    fmt.Println(completion)
}

