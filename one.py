from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    joke = None

    if request.method == "POST":
        # User mood input
        mood_text = request.form.get("mood")

        # Call API (simple joke API for now)
        url = "https://v2.jokeapi.dev/joke/Any"
        response = requests.get(url)
        data = response.json()

        if data["type"] == "single":
            joke = data["joke"]
        else:
            joke = data["setup"] + " ..." + data["delivery"]

    return render_template("index.html", joke=joke)

if __name__ == "__main__":
    app.run(debug=True)
