# Telegram Invite Redirect (Gumroad → Telegram)

Flask endpoint `/join` tạo **Telegram invite link 1 lần** và **redirect** khách vào channel ngay sau thanh toán (dùng với Gumroad Post-purchase Redirect).

## Chạy cục bộ

```bash
pip install -r requirements.txt

# Windows PowerShell
$env:BOT_TOKEN="TOKEN_THUC"
$env:CHAT_ID="-1001234567890"
$env:SECRET_KEY="optional_secret"   # tuỳ chọn

# Mac/Linux
export BOT_TOKEN="TOKEN_THUC"
export CHAT_ID="-1001234567890"
export SECRET_KEY="optional_secret"

# chạy dev
python -m flask --app app run --port 5000
# mở http://127.0.0.1:5000/join?k=optional_secret
```

## Deploy Render (tóm tắt)

1. Tạo repo GitHub chứa các file.
2. Render → New + → Web Service → Connect repo.
3. Environment: Python 3.x
4. Add Environment Variables:
   - BOT_TOKEN
   - CHAT_ID
   - SECRET_KEY (tuỳ chọn)
5. Start Command: `gunicorn app:app --preload --workers=2 --threads=4 --timeout=60`
6. Lấy URL public, vd: `https://ten-app.onrender.com/join?k=optional_secret`
7. Trong Gumroad Product → Post-purchase → Redirect to URL → dán URL trên.
