from marshmallow import Schema, fields


class PlainTaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    priority = fields.Int(required=True)
    status = fields.Str(required=True)
    start_date = fields.DateTime(required=False)
    end_date = fields.DateTime(required=False)
    minutes = fields.Int(required=False)


class TaskSchema(PlainTaskSchema):
    from app.schemas.category import PlainCategorySchema
    category_id = fields.Int(required=True, load_only=True)
    category = fields.Nested(PlainCategorySchema(), dump_only=True)
    from app.schemas.user import PlainUserSchema
    user_id = fields.Int(required=True, load_only=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)
