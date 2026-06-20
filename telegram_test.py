import requests



TOKEN = "8838421364:AAEqo6oR47chV895sgDG78-HKJc5NoxLb-0"

CHAT_ID = "957849521"



message = "Test Message"



url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"



requests.post(
url,
data={
"chat_id": CHAT_ID,
"text": message
}
)

print("Done")



