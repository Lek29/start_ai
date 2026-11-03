import os
from dotenv import load_dotenv
import anthropic


load_dotenv()
client = anthropic.Anthropic()


with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

messages = []
print("Бот-ассистент запущен. Введите ваш вопрос (или 'exit' для выхода):")

while True:
    user_input = input("\nВопрос: ")
    if user_input.lower() in ['exit', 'выход', 'quit']:
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.messages.create(
            model="claude-haiku-5-5", 
            max_tokens=300,
            system=system_prompt, 
            messages=messages
        )

        bot_reply = ""
        for block in response.content:
            if block.type == 'text':
                bot_reply = block.text
                break
        print(f"Бот: {bot_reply}")

        
        messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print(f"Ошибка API: {e}")
        messages.pop() 