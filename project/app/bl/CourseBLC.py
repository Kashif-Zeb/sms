from project.app.repositories.DepartmentRepository import DepartmentRepository
from project.app.repositories.courseRepository import CourseRepository
from project.app.db import db
from flask import request, jsonify
from project.app.models.Department import Department


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
