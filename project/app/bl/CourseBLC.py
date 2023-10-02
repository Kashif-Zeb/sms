from project.app.repositories.DepartmentRepository import DepartmentRepository
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
        if department_name:
            existing_department = DepartmentRepository.get_dept_name(
                session, department_name
            )

            if existing_department:
                existing_department.course.append(course_name)
                session.commit()
                return jsonify(
                    {
                        "message": f"course  {course_name} associated with Department {department_name}."
                    }
                )
        else:
            new_department = DepartmentRepository.add_dept(department_name)

            new_department.course.append(course_name)
            session.add(new_department)
            session.commit()
            return jsonify(
                {
                    "message": f"Department {department_name} created and associated with course {course_name}."
                }
            )
