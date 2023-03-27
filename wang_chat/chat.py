import openai


class chatGPT:

    api_key = "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"
    model = "gpt-3.5-turbo"
    role = "user"

    def __init__(self, api_key=""):
        if api_key == "":
            openai.api_key = self.api_key
        else:
            openai.api_key = api_key

    def completion_start(self, content="你好"):
        try:
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": self.role, "content": content}],
            )
        except Exception as e:
            print(e)
            return "请求发生错误，请在日志中查看或联系管理员！"

        

        if not completion['choices'][0]['message']['content']:
            return "请求发生错误，请在日志中查看或联系管理员！"
        return completion['choices'][0]['message']['content']


# chat = chatGPT()
# print(chat.completion_start("用以下列表中的新单词编写一个有趣的英文小故事，50单词以内，我需要在每次新单词出现时都在后面标注中文意思。"
#                               "然后将这个故事翻译成中文，我需要中文翻译的时候遇到对应的新单词也标注一下。最后列出所有新单词，词性和对应的"
#                               "中文意思：\nthanks"))