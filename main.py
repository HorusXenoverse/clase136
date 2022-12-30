from flask import Flask, jsonify, request
from dataArchivos import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"success"
    }), 200

@app.route("/planet1")
def planetIndex():
    name = request.args.get("name")
    namePlanet = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": namePlanet,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()