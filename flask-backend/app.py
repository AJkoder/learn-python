from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    if not data:
        return jsonify({"error": "Empty JSON provided"}), 400

    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)

    return jsonify({
        "message": "Task created",
        "task": task
    }), 201

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"]==task_id:
            return jsonify(task),200
    return jsonify({"error":"task not found"}),404
 
if __name__ == "__main__":
    app.run(debug=True)