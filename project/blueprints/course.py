import os
from flask import (
    Response,
    request,
    jsonify,
    send_file,
    send_from_directory,
    make_response,
)
from webargs.flaskparser import use_args
from project.app.schemas.courseSchema import CourseSchema
from project.app.schemas.DepartmentSchema import DepartmentSchema
from project.app.schemas.FileSchema import fileSchema
from flask import Blueprint, current_app
from project.app.models.student import Student
from project.app.models.Department import Department
from project.app.models.Teacher import Teacher
from project.app.models.Course import Course
from project.app.models.File import File
from project.app.db import db
from project.app.repositories.StudentRepository import StudentRepository
from marshmallow import fields
from project.app.bl.CourseBLC import CourseBLC
from werkzeug.utils import secure_filename

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


@bp.route("/uploadfile", methods=["POST"])
def uploadfile():
    file_data = fileSchema().load(request.files)
    uploaded_file = file_data["filename"]

    # Process the uploaded file, for example, save it to a directory
    filename = secure_filename(uploaded_file.filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    file_path = os.path.join(upload_folder, filename)
    uploaded_file.save(file_path)
    new = CourseBLC.uploading_file(filename, file_path)
    return new


@bp.route("/download", methods=["GET"])
@use_args({"file": fields.String()}, location="query")
def download_file(args):
    filename = args.get("file")
    file_path = CourseBLC.downloading(filename)
    print(file_path, filename)
    if file_path:
        # res = send_file(file_path, as_attachment=True, download_name=filename)
        # res1 = make_response(res)
        # res1.headers("text/plain")

        return send_file(
            file_path, as_attachment=True, download_name=filename, mimetype="text/plain"
        )

    else:
        return jsonify({"message": "file not found"})
