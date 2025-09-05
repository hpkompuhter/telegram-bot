import os, time, requests

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN env o'zgaruvchisi yo'q!")

API = f"https://api.telegram.org/bot{TOKEN}"

def send(chat_id, text):
    requests.post(f"{API}/sendMessage", json={"chat_id": chat_id, "text": text})

def handle_update(upd):
    msg = upd.get("message") or {}
    text = msg.get("text", "") or ""
    if text.startswith("/start"):
        first = (msg.get("from", {}) or {}).get("first_name") or "oshna"
        send(msg["chat"]["id"], f"Salom {first}!")

def main():
    offset = None
    while True:
        try:
            r = requests.get(f"{API}/getUpdates", params={"timeout": 50, "offset": offset}, timeout=60)
            data = r.json()
            for upd in data.get("result", []):
                offset = upd["update_id"] + 1
                handle_update(upd)
        except Exception as e:
            print("Xatolik:", e)
            time.sleep(2)

if __name__ == "__main__":
    main()
