from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    name = "Surawut"
    lastname = "Saithong-in"
    return f"Hello My name is {name} {lastname}"

@app.route("/game")
def game():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
