from app.connections.db import db
from app.models.base import BaseModel

"""
El nombre de las carpetas deben ir en singular o plural, estoy creando un proyecto en flask y quiero realizar las mejores practicas
"""


class TaskModel(BaseModel):
    """
        Table Model Task
    """
    __tablename__ = "task"
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime, nullable=True)
    minutes = db.Column(db.Integer, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), unique=False, nullable=False)
    category = db.relationship("CategoryModel", back_populates="tasks")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False)
    user = db.relationship("UserModel", back_populates="tasks")

    def __repr__(self):
        return f'<Task {self.name}>'

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category_id": self.category_id,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
