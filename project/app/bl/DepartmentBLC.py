from project.app.repositories.DepartmentRepository import DepartmentRepository
from project.app.db import db
from flask import request, jsonify
from project.app.models.Department import Department


class DepartmentBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_department_b(department_name, stu_name):
        session = DepartmentBLC.get_session()
        if department_name:
            existing_department = DepartmentRepository.get_dept_name(
                session, department_name
            )

            if existing_department:
                student = DepartmentRepository.get_stu_name(session, stu_name)
                if student:
                    if student in existing_department.student:
                        # return jsonify({existing_department.student})
                        return jsonify({"message": "student already in a dept"})
                    else:
                        existing_department.student.append(student)
                        session.commit()
                        return jsonify(
                            {
                                "message": f"Student {stu_name} associated with Department {department_name}."
                            }
                        )
                else:
                    return jsonify({"error": "No such student."})

            else:
                new_department = DepartmentRepository.add_dept(department_name)
                student = DepartmentRepository.get_stu_name(session, stu_name)
                if student:
                    new_department.student.append(student)
                    session.add(new_department)
                    session.commit()
                    return jsonify(
                        {
                            "message": f"Department {department_name} created and associated with Student {stu_name}."
                        }
                    )
                else:
                    return jsonify({"error": "No such student."})
        else:
            return jsonify({"error": "Department name not provided in JSON data."})

    @staticmethod
    def delete_dept(id):
        session = DepartmentBLC.get_session()
        department_D = DepartmentRepository.getdept(id, session)
        if not department_D:
            return jsonify({"message": f"{id} not found"})

        DepartmentRepository.delete_d(department_D, session)
