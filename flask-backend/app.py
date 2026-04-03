from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
current_user_id=None

class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    completed=db.Column(db.Boolean, default=False)

    user_id=db.Column(db.Integer, db.ForeignKey('user.id') nullable=False)
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/signup", methods=["POST"])
def signup():
    data=request.get_json()

    username=data.get("username")
    password=data.get("password")

    if not username or not password:
        return jsonify({"error":"Username and password required"}), 400
    
    existing_user=User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error":"User already exists"}), 400
    new_user=User(username=username,password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message":"User created successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    global current_user_id
    data=request.get_json()

    username=data.get("username")
    password=data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    user=User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"error":"User not found"}),404
    if user.password!=password:
        return jsonify({"error": "Invalid password"}), 401
    current_user_id=user.id
    return jsonify({
        "message": "Login successful",
    }), 200



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
    if not current_user_id:
        return jsonify({"error": "Login required"}), 401

    title = data.get("title")

    if not title or not isinstance(title, str) or title.strip() == "":
        return jsonify({"error": "Title must be a non-empty string"}), 400

    new_task = Task(
        title=title,
        completed=False,
        user_id=current_user_id
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "message": "Task created",
        "task": task_to_dict(new_task)
    }), 201

@app.route("/tasks",methods=["GET"])
def get_tasks():
    if not current_user_id:
        return jsonify({"error": "Login required"}), 401

    tasks = Task.query.filter_by(user_id=current_user_id).all()

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    tasks = Task.query.filter_by(user_id=user_id).all()

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
        title = data["title"]

        if not isinstance(title, str) or title.strip() == "":
            return jsonify({"error": "Title must be a non-empty string"}), 400

        task.title = title
    if "completed" in data:
        completed = data["completed"]

        if not isinstance(completed, bool):
            return jsonify({"error": "Completed must be true or false"}), 400

        task.completed = completed
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