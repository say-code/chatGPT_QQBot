
import requests

url = "https://api.openai.com/v1/chat/completions"

prompt = "你好"
params = {
    "messages": [{"role": "user", "content": "很高兴见到你"}],
    "max_tokens": 120,
    "n": 1,
    "stop": None,
    "model": "gpt-3.5-turbo",

}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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",


}

response = requests.post(url, json=params, headers=headers)

if response.ok:
    # print(response.json())
    result = response.json()['choices'][0]['message']['content']
    print(result)
else:
    print(response.json())
    print("请求失败")
