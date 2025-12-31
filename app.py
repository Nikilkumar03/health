import os
from flask import Flask, jsonify

PORT = os.getenv("APP_PORT")

if not PORT:
    raise RuntimeError("APP_PORT environment variable is not set")

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        app="port-demo-app",
        port=int(PORT)
    )

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))
