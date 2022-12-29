from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    name = "Surawut"
    lastname = "Saithong-in"
    # msg = f"Hello My name is {name} {lastname}"
    return render_template("index.html")


@app.route("/game")
def game():
    return render_template("game/index.html")


@app.route("/home")
def home():
    name = request.args.get("name", "Surawut")
    profile_name = f"name = {name}"
    return render_template("home/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
