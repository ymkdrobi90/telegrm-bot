from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8838421364:AAEqo6oR47chV895sgDG78-HKJc5NoxLb-0"
CHAT_ID = "-5361656863"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    if data and "message" in data:
        message = data["message"]
    else:
        message = request.get_data(as_text=True) or "TradingView Alert"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print(response.text)

    return "OM_BOT_TEST", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
