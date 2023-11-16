from marshmallow import Schema, fields


class PlainCategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=False)


class CategorySchema(PlainCategorySchema):
    from app.schemas.task import PlainTaskSchema
    tasks = fields.List(fields.Nested(PlainTaskSchema()), dump_only=True)
