from flask import Flask, request

app = Flask(__name__)

# Route trang chủ
@app.route("/")
def home():
    return "Hello from Render + Flask!"

# Route '/join' để xử lý tham số 'k' từ URL
@app.route("/join")
def join():
    k = request.args.get('k')  # Lấy tham số 'k' từ URL
    if k:
        return f"Chào bạn, kênh Telegram của bạn là: {k}"  # Hiển thị giá trị của tham số k
    else:
        return "Không có mã kênh!"  # Nếu không có tham số k, trả về thông báo này

if __name__ == "__main__":
    app.run(debug=True)

