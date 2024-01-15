import os

import openai
from fastapi import APIRouter, Header
from pydantic import BaseModel


class Prompt(BaseModel):
    msg: str

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}}
)

@router.post("/")
async def chat(prompt: Prompt, openai_org: str = Header(...), openai_key: str = Header(...)):
    print(prompt.msg)
    max_attempts = 3  # Número máximo de tentativas
    attempt = 0

    while attempt < max_attempts:
        try:
            openai.api_key = openai_key
            openai.organization = openai_org

            chatgpt = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente do projeto QUIZ do canal Jogatinando!"},
                    {"role": "user", "content": prompt.msg},
                ]
            )

            result = chatgpt.choices[0].message.content

            return {"response": result}
        except openai.APIError as e:
            attempt += 1
            print(f"Tentativa {attempt} falhou. Motivo: {e}")

    return {"error": "Falha ao se comunicar com a OpenAI após várias tentativas."}
