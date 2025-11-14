import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation = [
    {"role": "system", "content": "Você é um assistente que organiza mídias usando IA."},
]

def chat():
    print("=== Chat GPT no Terminal ===")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando chat...")
            break

        conversation.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        print(f"GPT: {reply}")
        conversation.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()
