from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

# Modelo de dados (antes estava em models.py, mas podemos deixar aqui pra simplificar)
class Data(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/messages/")
def create_message(data: Data):
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if not bot_token or not chat_id:
        return {"status": "error", "detail": "BOT_TOKEN ou CHAT_ID não configurados"}

    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": data.message,
            "parse_mode": "HTML"
        }
    )
    

    return {
        "status": "success" if response.status_code == 200 else "error",
        "telegram_response": response.json(),
        "telegram_url": f"https://api.telegram.org/bot{bot_token}/sendMessage"
    }