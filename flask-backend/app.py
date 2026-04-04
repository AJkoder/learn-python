from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "mysecretkey"

db = SQLAlchemy(app)

# ---------------- MODELS ----------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()


# ---------------- JWT HELPER ----------------
def get_current_user():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    try:
        token = auth_header.split(" ")[1]
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return data["user_id"]
    except:
        return None


# ---------------- AUTH ROUTES ----------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if user.password != password:
        return jsonify({"error": "Invalid password"}), 401

    token = jwt.encode({
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200


# ---------------- UTILITY ----------------
def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }


# ---------------- TASK ROUTES ----------------
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Login required"}), 401

    title = data.get("title")

    if not title or not isinstance(title, str) or title.strip() == "":
        return jsonify({"error": "Invalid title"}), 400

    new_task = Task(title=title, completed=False, user_id=user_id)

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"task": task_to_dict(new_task)}), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    user_id = get_current_user()

    if not user_id:
        return jsonify({"error": "Login required"}), 401

    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify({"tasks": [task_to_dict(t) for t in tasks]}), 200


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Login required"}), 401

    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    if task.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()

    if "title" in data:
        title = data["title"]
        if not isinstance(title, str) or title.strip() == "":
            return jsonify({"error": "Invalid title"}), 400
        task.title = title

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify({"error": "Invalid completed value"}), 400
        task.completed = data["completed"]

    db.session.commit()

    return jsonify({"task": task_to_dict(task)}), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    user_id = get_current_user()
    if not user_id:
        return jsonify({"error": "Login required"}), 401

    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    if task.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)