from flask import Flask, render_template
from forms import simpleForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "flask_secret_key"


@app.route("/")
def index():
    name = "Surawut"
    lastname = "Saithong-in"
    # msg = f"Hello My name is {name} {lastname}"
    return render_template("index.html")


@app.route("/game", methods=["GET"])
def game():
    return render_template("game/index.html")


@app.route("/home", methods=["GET"])
def home():

    return render_template("home/index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = simpleForm()

    return render_template("login/index.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
