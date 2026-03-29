from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to my Flask backend!"

# About route
@app.route("/about")
def about():
    return "This backend is built using Flask."

# API route (JSON response)
@app.route("/api")
def api():
    data = {
        "name": "realchamp",
        "role": "Backend Developer",
        "phase": "Phase 3"
    }
    return jsonify(data)

# Dynamic route (GET parameter)
@app.route("/greet")
def greet():
    name = request.args.get("name")

    if name:
        return jsonify({"message": f"Hello, {name}!"})
    else:
        return jsonify({"message": "Hello, Guest!"})


if __name__ == "__main__":
    app.run(debug=True)