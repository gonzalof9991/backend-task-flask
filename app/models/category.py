from app.connections.db import db
from app.models.base import BaseModel


class CategoryModel(BaseModel):
    """
        Table Model Category
    """
    __tablename__ = "category"
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    tasks = db.relationship("TaskModel", back_populates="category", lazy="dynamic")

    def __repr__(self):
        return f'<Category {self.name}>'

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "tasks": self.tasks,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
