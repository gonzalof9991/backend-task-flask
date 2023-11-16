from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.models import TaskModel
from app.schemas.task import TaskSchema

blp = Blueprint("Task", __name__, description="Operations on tasks")


@blp.route("/task/<int:task_id>")
class Task(MethodView):
    @blp.response(200, TaskSchema)
    def get(self, task_id):
        print("Task GET")
        data = TaskModel.get_by_id(task_id)
        return jsonify(data)

    @blp.arguments(TaskSchema)
    @blp.response(200, TaskSchema)
    def update(self, task_data):
        task = TaskModel.get_by_id(task_data["id"])
        task.name = task_data["name"]
        task.description = task_data["description"]
        task.priority = task_data["priority"]
        task.status = task_data["status"]
        task.end_date = task_data["end_date"]
        task.minutes = task_data["minutes"]
        try:
            task.update_to_db()
            task.save_to_db()
        except SQLAlchemyError:
            abort(500, message="An error occurred while updating the task.")

        return task


@blp.route("/task/")
class TaskList(MethodView):
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskModel.get_all()

    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self, task_data):
        print(task_data)
        task = TaskModel(**task_data)
        try:
            task.save_to_db()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the task.")

        return task

    @blp.response(200)
    def delete(self):
        TaskModel.delete_all()
        return {"message": "All tasks deleted successfully."}


