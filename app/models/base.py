from datetime import datetime

from app.connections.db import db
from app.schemas.user import UserSchema


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(80), unique=False, nullable=False, default="active")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.deleted_at = datetime.now()
        db.session.commit()

    def update_to_db(self):
        self.updated_at = datetime.now()
        db.session.commit()

    @classmethod
    def get_all(cls: db.Model) -> list[any]:
        return cls.query.filter_by(deleted_at=None).all()

    @classmethod
    def get_by_id(cls: db.Model, id: int) -> any:
        return cls.query.filter_by(id=id, deleted_at=None).first()

    @classmethod
    def delete_all(cls: db.Model) -> None:
        items = cls.query.all()
        for item in items:
            item.delete_from_db()
            db.session.commit()
        print(f"All {cls.__name__} deleted successfully.")
