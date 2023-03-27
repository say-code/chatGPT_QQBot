from nonebot import on_message, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.internal.params import ArgPlainText
from chat import chatGPT

matcher = on_keyword({'启动chatGPT', '连接大脑'})
chat = chatGPT()
matcher_english = on_keyword({'记单词'})
matcher_word = on_keyword({'每日一句'})
session_dit = {}
@matcher.got("arg",prompt="输入\"结束对话\"以结束对话")
async def start_chat(event: Event, bot:Bot, arg: str = ArgPlainText()):
    if not arg == "结束对话":
        print(arg)

        if str(event.get_user_id) not in session_dit.keys():
            session_dit[str(event.get_user_id)] = "\n"
        else:
            context_lines = session_dit[str(event.get_user_id)].split("\n")[-10:]
            session_dit[str(event.get_user_id)] = "\n".join(context_lines)
            prompt = f"用户：{arg}\nChatGPT:"
            message = chat.completion_start(prompt)
            session_dit[str(event.get_user_id)] += f"用户：{arg}\nChatGPT:{message}\n"
            await matcher.reject(
                message
            )

@matcher_english.got("arg", prompt="请输入你需要记忆的数个英文单词，以空格隔开")
async def start_by(arg: str = ArgPlainText()):
    await matcher.send(
        '正在使用gpt生成句子哦，请耐心等待=^▽^='
    )
    await matcher.send(
        chat.completion_start("用以下列表中的新单词编写一个有趣的英文小故事，50单词以内，我需要在每次新单词出现时都在后面标注中文意思。"
                              "然后将这个故事翻译成中文，我需要中文翻译的时候遇到对应的新单词也标注一下。最后列出所有新单词，词性和对应的"
                              "中文意思：\n"+arg)
    )

@matcher_word.handle()
async def start_word():
    await matcher.send(
        '将会生成包含若干个6级词汇的句子哦，请耐心等待=^▽^='
    )
    await matcher.send(
        chat.completion_start("请生成一句话，包含若干个英语6级词汇，然后附上整段话的中文翻译，最后附上所有生词的词性和翻译")
    )





