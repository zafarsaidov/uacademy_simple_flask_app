from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv("/tmp/.env")

app = Flask(__name__)
version = os.getenv("VERSION", "1.1.0")
node = os.getenv("NODE", "dev")


@app.route("/api/v1/user/sum", methods=["POST"])
def start():
    a = request.json.get("a", "")
    b = request.json.get("b", "")
    d = {
        "a": a,
        "b": b
    }
    return jsonify(d)

@app.route("/api/v1/get/version", methods=["GET"])
def getversion():
    return jsonify({ "version": version, "node": node})

@app.route("/hi")
def hi():
    return "Hi"

@app.route("/bye")
def bye():
    return "Bye"

app.run(host="0.0.0.0", port=8888)