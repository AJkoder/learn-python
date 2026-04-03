from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    completed=db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

def task_to_dict(task):
    return {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    title = data.get("title")

    if not title or not isinstance(title, str) or title.strip() == "":
        return jsonify({"error": "Title must be a non-empty string"}), 400

    new_task = Task(
        title=title,
        completed=False
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "message": "Task created",
        "task": task_to_dict(new_task)
    }), 201

@app.route("/tasks",methods=["GET"])
def get_tasks():
    tasks=Task.query.all()

    result=[task_to_dict(task) for task in tasks]   
    return jsonify({"tasks": result}),200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task_to_dict(task)), 200

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data=request.get_json()

    if data is None:
        return jsonify({"error":"Invalid or missing json"}), 400
    task=Task.query.get(task_id)

    if not task:
        return jsonify({"error":"Task not found"}), 404
    
    if "title" in data:
        task.title=data["title"]
    if "completed" in data:
        task.completed=data["completed"]
    db.session.commit()

    return jsonify({
        "message": "task updated",
        "task": task_to_dict(task)
    }), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task=Task.query.get(task_id)

    if not task:
        return jsonify({"error":"Task not found"}), 404
    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)