from flask import Flask, request, render_template
from pyautogui import hotkey

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/buttons")
def buttons():
    return render_template("buttons.html")


@app.route("/press", methods=["GET"])
def press():
    mod1 = request.args.get("mod1")
    mod2 = request.args.get("mod2")
    key = request.args.get("key")
    hotkey(mod1, mod2, key)
    print(f"{mod1} {mod2} {key} pressed.")
    return "ok."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234, debug=True)