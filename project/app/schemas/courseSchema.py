from marshmallow import (
    Schema,
    fields,
    validate,
)


class CourseSchema(Schema):
    name = fields.String(
        validate=validate.Length(min=1, max=25),
        required=True,
        error_messages={"required": "Name field cannot be empty."},
    )
