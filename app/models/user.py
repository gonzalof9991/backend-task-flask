from app.models.base import BaseModel
from app.connections.db import db


class UserModel(BaseModel):
    __tablename__ = 'user'
    name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)
    tasks = db.relationship("TaskModel", back_populates="user", lazy="dynamic")

    def __repr__(self):
        return f'<User {self.name}>'

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name
        }
