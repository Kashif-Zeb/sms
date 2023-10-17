from marshmallow import (
    Schema,
    fields,
    validate,
)


class fileSchema(Schema):
    filename = fields.Field(
        required=True,
        error_messages={"required": "file field cannot be empty."},
    )
    # path=fields.String(validate=validate.Length(max=100),required=T)
