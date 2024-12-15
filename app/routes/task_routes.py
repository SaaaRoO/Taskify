from flask import Blueprint, request, jsonify
from models.models import Task, User
from db.database import db
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    tasks = Task.query.join(User).filter(User.username == current_user).all()
    return jsonify([{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks])

@task_bp.route("/tasks", methods=["POST"])
@jwt_required()
def add_task():
    current_user = get_jwt_identity()
    data = request.json
    new_task = Task(title=data["title"], user_id=User.query.filter_by(username=current_user).first().id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"msg": "Task added successfully!"}), 201

@task_bp.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    task.completed = data.get("completed", task.completed)
    db.session.commit()
    return jsonify({"msg": "Task updated successfully!"})

@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted successfully!"})
