from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    email = fields.Str(required=True)
    status = fields.Boolean(required=False)
    role = fields.Str(required=True)


class UserSchema(PlainUserSchema):
    from app.schemas.task import PlainTaskSchema
    task_id = fields.Int(required=False, load_only=True)
    task = fields.Nested(PlainTaskSchema(), dump_only=True)
