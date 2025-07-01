from flask import Blueprint, request, jsonify, abort
from app.models.task import Task
from app.extensions import db
from  app.models.gamefication import Gamefication  


task_bp = Blueprint("tasks", __name__)
@task_bp.route("/", methods=["GET"])
def get_tasks():
    """Get aall tasks."""
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]),200

@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get a single task by its ID."""
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict()), 200

@task_bp.route("/", methods=["POST"])
def create_task():
    """
    Create a new task.
    Expected JSON:
    {
        "title": "Task title",
        "description": "Optional description"
    }
    """
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    
    new_task = Task(
        title=data["title"],
        description=data.get("description", "")
    )
    
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """ 
    Update a task by its ID.
    JSON fields allowed: title, description, completed
    """
    task = Task.query.get_or_404(task_id)
    data=request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    was_completed = task.completed  #status anterior

    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "completed" in data:
        task.completed = data["completed"]
    
    db.session.commit()    
    
    if not was_completed and task.completed:
        gamefication = Gamefication.query.first()
        if not gamification:
            gamefication = Gamefication()
            db.session.add(gamefication)
        gamefication.task_completed += 1
        gamefication.points +=10
        gamification.level = 1 + gamefication.points // 100
        gamefication.last_update = datetime.utcnow()
        db.session.commit()
    return jsonify(task.to_dict()), 200

@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task by its ID."""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200

@task_bp.route("/gamefication", methods=["GET"])
def get_gamefication():
    """Get the gamefication status."""
    gamefication = Gamefication.query.first()
    if not gamefication:
        return jsonify({
             "points": 0,
            "level": 1,
            "tasks_completed": 0
            }), 200
    return jsonify(
        {"points": gamefication.points,
        "level": gamefication.level,
        "tasks_completed": gamefication.tasks_completed}), 200