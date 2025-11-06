import os
import json
from flask import Flask, request
import requests

app = Flask(__name__)

# --- YOUR BOT TOKEN (from GitHub secret) ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

@app.route('/')
def home():
    return "Bot is running!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text.lower() == "/start":
            send_message(chat_id, "🚀 Welcome to Cosmic ! Type 'play' to begin your adventure.")
        elif text.lower() == "play":
            send_message(chat_id, "🌌 You find yourself aboard a starship entering unknown space...")
        else:
            send_message(chat_id, "✨ Type 'play' to start your intergalactic quest!")
    return "OK", 200

def send_message(chat_id, text):
    url = TELEGRAM_API_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
