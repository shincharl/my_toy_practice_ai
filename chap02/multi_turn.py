from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=messages # 대화 기록을 입력으로 저장
    )
    return response.choices[0].message.content # 생성된 내용의 응답 반환

messages = [
    {"role": "system", "content":"너는 사용자를 도와주는 상담사야."}
] # 초기 시스템 메시지 설정

while True:
    user_input = input("사용자: ") # 사용자 입력받기

    if user_input == "exit":
        break

    messages.append({"role":"user", "content": user_input})
    ai_response = get_ai_response(messages)
    messages.append({"role":"assistant", "content": ai_response})
    print("AI: " + ai_response)