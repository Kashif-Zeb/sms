from marshmallow import (
    Schema,
    fields,
    validate,
)


class StudentSchema(Schema):
    name = fields.String(
        validate=validate.Length(min=3, max=25),
        required=True,
        error_messages={"required": "Name field cannot be empty."},
    )
    email = fields.Email(
        required=True, error_messages={"required": "Email field cannot be empty."}
    )
    address = fields.String(
        required=True, error_messages={"required": "Address field cannot be empty."}
    )
    number = fields.String(
        validate=validate.Length(min=5, max=20),
        required=True,
        error_messages={"required": "Number field cannot be empty."},
    )
