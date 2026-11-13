from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="th">
<meta charset="utf-8">
<title>ส่งข้อความ</title>
<h1>ส่งข้อความ</h1>
<form method="post">
  <input name="message" placeholder="พิมพ์ข้อความ" required>
  <button type="submit">ส่ง</button>
</form>
{% if message %}<p>ข้อความที่ได้รับ: {{ message }}</p>{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        message = request.form.get("message", "")
        with open("logs/log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} {message}\n")
    return render_template_string(PAGE, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
