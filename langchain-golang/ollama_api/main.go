package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

// 请求结构
type OllamaRequest struct {
	Model    string    `json:"model"`
	Stream   bool      `json:"stream"`
	Messages []Message `json:"messages"`
}

type Message struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

// 响应结构（根据Ollama流式格式）
type OllamaResponse struct {
	Done    bool    `json:"done"`
	Message Message `json:"message"`
}

func main() {
	r := gin.Default()

	r.GET("/stream", func(c *gin.Context) {
		prompt := c.Query("prompt")
		if prompt == "" {
			c.JSON(http.StatusBadRequest, gin.H{"error": "prompt is required"})
			return
		}

		reqBody := OllamaRequest{
			Model:  "qwen2:7b", // 可根据你本地加载的模型名修改
			Stream: true,
			Messages: []Message{
				{
					Role:    "user",
					Content: prompt,
				},
			},
		}

		data, err := json.Marshal(reqBody)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "marshal request failed"})
			return
		}

		resp, err := http.Post("http://localhost:11434/api/chat", "application/json", bytes.NewBuffer(data))
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "failed to call ollama"})
			return
		}
		defer resp.Body.Close()

		// 设置为SSE响应
		c.Header("Content-Type", "text/event-stream")
		c.Header("Cache-Control", "no-cache")
		c.Header("Connection", "keep-alive")

		scanner := bufio.NewScanner(resp.Body)
		for scanner.Scan() {
			line := scanner.Text()
			var ollamaResp OllamaResponse
			if err := json.Unmarshal([]byte(line), &ollamaResp); err != nil {
				continue // 跳过解析失败的数据
			}

			if ollamaResp.Message.Content != "" {
				// 将内容作为SSE事件发送到客户端
				c.Writer.Write([]byte("data: " + ollamaResp.Message.Content + "\n\n"))
				c.Writer.Flush()
			}

			if ollamaResp.Done {
				break
			}
		}

		if err := scanner.Err(); err != nil {
			log.Println("stream read error:", err)
		}
	})

	r.Run(":8080")
}
