from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)