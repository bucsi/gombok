import json
from pyautogui import hotkey
from flask import Flask, request, render_template

app = Flask(__name__)

try:
    with open('config.json', 'r') as f:
        config = json.loads(f.read())
except:
    print("Could not load config.json. Does the file exist?")


@app.route("/")
def buttons():
    return render_template("buttons.html", buttons=config["buttons"])


@app.route("/press", methods=["GET"])
def press():
    mod1 = request.args.get("mod1")
    mod2 = request.args.get("mod2")
    key = request.args.get("key")
    hotkey(mod1, mod2, key)
    print(f"{mod1} {mod2} {key} pressed.")
    return "ok."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])