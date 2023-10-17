from project.app.models.File import File
from project.app.repositories.DepartmentRepository import DepartmentRepository
from project.app.repositories.courseRepository import CourseRepository
from project.app.db import db
from flask import app, current_app, request, jsonify, send_from_directory
from project.app.models.Department import Department
import os


class CourseBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_course(department_name, course_name):
        session = CourseBLC.get_session()
        # breakpoint()
        if course_name:
            exist = CourseRepository.get_course_name(session, course_name)
            if exist:
                department = DepartmentRepository.get_dept_name(
                    session, department_name
                )
                if department:
                    if department in exist.department:
                        return (
                            jsonify(
                                {
                                    "message": f"Course '{course_name}' is already associated with '{department_name}'."
                                }
                            ),
                            200,
                        )
                    exist.department.append(department)
                    session.commit()
                    return (
                        jsonify(
                            {
                                "message": f"course {course_name} associated with {department_name}"
                            }
                        ),
                        200,
                    )
                else:
                    return jsonify({"message": "department not found"}), 404

            else:
                newcourse = CourseRepository.add_new_course(course_name)
                department = DepartmentRepository.get_dept_name(
                    session, department_name
                )
                if department:
                    newcourse.department.append(department)
                    session.add(newcourse)
                    session.commit()
                    return (
                        jsonify(
                            {
                                "message": f"new {department_name} is created and associated with {course_name}"
                            }
                        ),
                        200,
                    )
                else:
                    return jsonify({"message": "department not found"}), 404
        else:
            return jsonify({"error": "Department name not provided in JSON data."})

    @staticmethod
    def uploading_file(filename, file_path):
        CourseRepository.add_file_db(filename, file_path)
        return jsonify({"file saved": filename}), 201
        # Save the file information in the database
        # db.session.add(File(filename=filename))
        # db.session.commit()

    @staticmethod
    def downloading(filename):
        session = CourseBLC.get_session()
        # breakpoint()
        if filename:
            getname = CourseRepository.get_file(filename, session)
            if getname:
                absolute_upload_folder = os.path.abspath(
                    current_app.config["UPLOAD_FOLDER"]
                )
                file_path = os.path.join(absolute_upload_folder, getname)

                # print("Full File Path:", file_path)
                # print(getname)
                if os.path.exists(file_path):
                    return file_path
