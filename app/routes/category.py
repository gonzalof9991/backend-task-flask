from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.models import CategoryModel
from app.schemas.category import CategorySchema

blp = Blueprint("Category", __name__, description="Operations on Categories")


@blp.route("/category/<int:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self):
        print("Task GET")


@blp.route("/category/")
class CategoryList(MethodView):

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        print("TaskList GET")
        data = CategoryModel.query.all()
        print(data)
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, category_data):
        print("TaskList POST")
        print(category_data, 'task_data')
        category = CategoryModel(**category_data)
        try:
            category.save_to_db()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the task.")

        return category
