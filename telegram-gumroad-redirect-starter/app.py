import os
import requests
from flask import Flask, redirect, jsonify, make_response, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # e.g., -1001234567890
SECRET_KEY = os.getenv("SECRET_KEY")  # optional: set to a random string

app = Flask(__name__)

@app.get("/join")
def join():
    # Optional simple guard: require ?k=SECRET_KEY if SECRET_KEY is set
    if SECRET_KEY:
        if request.args.get("k") != SECRET_KEY:
            return make_response(("Unauthorized", 401))

    if not BOT_TOKEN or not CHAT_ID:
        return make_response(("Server chưa cấu hình BOT_TOKEN/CHAT_ID", 500))

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/createChatInviteLink"
    payload = {
        "chat_id": CHAT_ID,
        "member_limit": 1  # chỉ dùng được 1 lần
        # Có thể thêm "expire_date": <epoch_seconds> nếu muốn thời hạn
    }

    try:
        r = requests.post(url, json=payload, timeout=15)
        data = r.json()
    except Exception as e:
        return make_response((f"Lỗi gọi Telegram API: {e}", 500))

    if not data.get("ok"):
        # Trả nguyên thông báo lỗi từ Telegram để dễ debug
        return make_response((f"Telegram trả lỗi: {data}", 500))

    invite_link = data["result"]["invite_link"]
    # 302 redirect sang link mời (tự động mở Telegram)
    return redirect(invite_link, code=302)

@app.get("/")
def health():
    return jsonify({"ok": True, "msg": "service up"})
