from flask import Flask, render_template, request, jsonify
from utils.api_client import send_request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/test", methods=["POST"])
def test_api():
    data = request.get_json()

    url = data.get("url")
    method = data.get("method", "GET")
    payload = data.get("payload", {})

    if not url:
        return jsonify({"error": "URL is required"}), 400

    result = send_request(url, method, payload)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)