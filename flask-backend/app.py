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

@app.route("/tasks/<int:task_id>",methods=["PUT"])
def update_task(task_id):
    data=request.get_json()
    if data is None:
        return jsonify({"error":"Invalid or missing JSON"}),400
    for task in tasks:
        if task["id"]==task_id:
            if "title" in data:
                task["title"]=data["title"]
            if "completed" in data:
                task["completed"]=data["completed"]
            return jsonify({
                "message": "Task Updated",
                "task": task
            }), 200
    return jsonify({"error":"Task not found"}), 404

 
if __name__ == "__main__":
    app.run(debug=True)