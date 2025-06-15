
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def hello():
    return jsonify({"message": "Lock'd In backend running via Vercel Serverless!"})
