from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Hello"
    })

@app.route("/about")
def about():
    return jsonify({
        "status": "success",
        "message": "About Page"
    })

@app.route("/status")
def status():
    return jsonify({
        "status": "success",
        "message": "Server is running"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "name": "realchamp",
        "phase": "Phase 3",
        "goal": "Backend Developer"
    })

@app.route("/api/greet")
def greet():
    name = request.args.get("name", "Guest")

    return jsonify({
        "status": "success",
        "message": f"Hello, {name}"
    })

if __name__ == "__main__":
    app.run(debug=True)