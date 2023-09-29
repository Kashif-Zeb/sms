from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.StudentSchema import StudentSchema
from project.app.schemas.DepartmentSchema import DepartmentSchema
from flask import Blueprint
from project.app.models.student import Student
from project.app.models.Department import Department
from project.app.models.Teacher import Teacher
from project.app.db import db
from project.app.repositories.StudentRepository import StudentRepository
from marshmallow import fields, Schema, validate
from project.app.bl.DepartmentBLC import DepartmentBLC

bp = Blueprint("department", __name__)


class StudentNameSchema(Schema):
    name = fields.String(
        validate=validate.Length(min=3, max=25),
        required=True,
        error_messages={"required": "Name field cannot be empty."},
    )


@bp.route("/add_department", methods=["POST"])
def add_department():
    try:
        department_data = request.get_json()
        student_schema = StudentNameSchema()
        department_schema = DepartmentSchema()

        stu_name = student_schema.load({"name": department_data.get("sname")})

        department_name = department_schema.load({"name": department_data.get("dname")})

        result = DepartmentBLC.add_department_b(
            department_name["name"], stu_name["name"]
        )

        return result, 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 422


@bp.route("/delete_department", methods=["Delete"])
@use_args({"id": fields.Integer()}, location="query")
def delete_department(args):
    DepartmentBLC.delete_dept(**args)
    return jsonify({"message": f"department  deleted  successfully"})
