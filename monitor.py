import os
import json
import urllib.request
import urllib.parse

token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

url = f"https://api.telegram.org/bot{token}/sendMessage"

data = urllib.parse.urlencode({
    "chat_id": chat_id,
    "text": "✅ Zilina Terminy: бот подключён! Готовим мониторинг свободных записей."
}).encode()

request = urllib.request.Request(url, data=data)

with urllib.request.urlopen(request, timeout=20) as response:
    result = json.loads(response.read())

if not result.get("ok"):
    raise RuntimeError("Telegram не подтвердил отправку сообщения")

print("Уведомление успешно отправлено!")
