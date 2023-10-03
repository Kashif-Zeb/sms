from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.StudentSchema import StudentSchema
from flask import Blueprint
from project.app.models.student import Student
from project.app.models.Department import Department
from project.app.models.Teacher import Teacher
from project.app.models.Course import Course
from project.app.db import db
from project.app.repositories.StudentRepository import StudentRepository
from marshmallow import fields
from project.app.bl.StudentBLC import StudentBLC

bp = Blueprint("student", __name__)


@bp.route("/add_student", methods=["POST"])
@use_args(StudentSchema, location="json")
def add_student(args):
    # breakpoint()
    try:
        student = Student(**args)

        StudentRepository.add_student(student)
        return jsonify({"message": f"student{student.name} add successfullly "})
    except Exception as e:
        return ({"error": str(e)}), 422


@bp.route("/get_single_student", methods=["GET"])
@use_args({"id": fields.Integer()}, location="query")
def get_single_student(args):
    try:
        student = StudentBLC.get_student(**args)
        student_schema = StudentSchema()
        return student_schema.dump(student), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 422


@bp.route("/update_student", methods=["PUT"])
@use_args({"id": fields.Integer()}, location="query")
@use_args(StudentSchema, location="json")
def update_student(query_args, student_data):
    try:
        student_id = query_args.get("id")
        StudentBLC.updating_student(student_id, student_data)
        # db.session.commit()
        return jsonify({"message": f"student {student_id} is updated "}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 422


@bp.route("/update_student2", methods=["PUT"])
@use_args({"id": fields.Integer()}, location="query")
# @use_args(StudentSchema, location="json")
def update_student2(args):
    try:
        student_id = args.get("id")
        student_data = request.get_json()
        StudentSchema().load(student_data)
        StudentBLC.updating_student2(student_id, student_data)
        # db.session.commit()
        return jsonify({"message": f"student {student_id} is updated "}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 422


@bp.route("/get_student", methods=["GET"])
def get_student():
    try:
        data = StudentRepository.get_all_student_q()
        std = StudentSchema(many=True)
        return jsonify(std.dump(data))
    except Exception as e:
        return jsonify({"Error": str(e)}), 422


@bp.route("/get_single_students_data", methods=["GET"])
@use_args({"id": fields.Integer()}, location="query")
def alldetails(args):
    try:
        student = StudentBLC.get_student_data(**args)
        std = StudentSchema()
        department_names = [department.name for department in student.department]
        teacher_name = [teacher.name for teacher in student.teacher]
        return jsonify(
            {
                "student": std.dump(student),
                "department": department_names,
                "teacher": teacher_name,
            }
        )
    except Exception as e:
        return jsonify({"Error": str(e)}), 422


@bp.route("/delete_student", methods=["DELETE"])
@use_args({"id": fields.Integer()}, location="query")
def delete_student(args):
    try:
        StudentBLC.delete_student(**args)
        return jsonify({"message": f"student {args} deleted successfully"})
    except Exception as e:
        return jsonify({"Error": str(e)}), 422


@bp.route("/Search", methods=["GET"])
@use_args({"se": fields.String()}, location="query")
def search(args):
    # se = request.get_json("search")
    result = StudentBLC.searching(**args)
    return jsonify({"searched": result})
