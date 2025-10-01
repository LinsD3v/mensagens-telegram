from fastapi import FastAPI
from models import Data
import os
import requests
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/messages/")
def create_message(data: Data):
    bot_token = os.getenv("BOT-TOKEN")
    chat_id = os.getenv("CHAT-ID")

    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        json={"chat_id": chat_id, "text": data.message, "parse_mode": "HTML"}
    )

    return {"status": "success" if response.status_code == 200 else "error"}

handler = Mangum(app)