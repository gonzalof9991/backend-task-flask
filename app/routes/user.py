from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from app.models import UserModel
from app.schemas.user import UserSchema
from app.utils import PasswordUtils

blp = Blueprint("User", __name__, description="Operations on users")


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        print("User GET")
        data = UserModel.get_by_id(user_id)
        return jsonify(data)


@blp.route("/user/")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        password_hash = PasswordUtils.hash_password(user_data["password"])
        print(password_hash)
        user = UserModel(
            name=user_data["name"],
            last_name=user_data["last_name"],
            username=user_data["username"],
            password=password_hash,
            email=user_data["email"],
            role=user_data["role"],
        )
        try:
            user.save_to_db()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the task.")

        return user
