from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.courseSchema import CourseSchema
from project.app.schemas.DepartmentSchema import DepartmentSchema
from flask import Blueprint
from project.app.models.student import Student
from project.app.models.Department import Department
from project.app.models.Teacher import Teacher
from project.app.models.Course import Course
from project.app.db import db
from project.app.repositories.StudentRepository import StudentRepository
from marshmallow import fields
from project.app.bl.CourseBLC import CourseBLC

bp = Blueprint("course", __name__)


@bp.route("/associate_course", methods=["POST"])
def addcourse():
    try:
        course = request.get_json()
        a = course.get("dname")
        b = course.get("cname")
        DS = DepartmentSchema()
        CS = CourseSchema()
        department_name = DS.load({"name": a})
        course_name = CS.load({"name": b})
        result = CourseBLC.adding_course(department_name["name"], course_name["name"])
        return result
    except Exception as e:
        return jsonify({"Error": str(e)}), 422
