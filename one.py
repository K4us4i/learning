from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        mood_text = request.form.get("mood")

        # Sentiment API URL
        url = "https://sentim-api.onrender.com/api/v1/"

        headers = {"Content-Type": "application/json"}
        payload = {"text": mood_text}

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        # Sentiment result: positive / negative / neutral
        result = data["result"]["type"]

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
