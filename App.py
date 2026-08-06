from flask import Flask, request
import requests
import os

app = Flask(__name__)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


@app.route("/", methods=["GET"])
def home():
    return "WhatsApp AI Bot is Running!"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    print(data)

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
