from project.app.models.Department import Department
from project.app.db import db
from project.app.models.student import Student


class DepartmentRepository:
    @staticmethod
    def get_dept_name(session, department_name):
        result = (
            session.query(Department).filter(Department.name == department_name).first()
        )
        return result

    @staticmethod
    def get_stu_name(session, stu_name):
        result = session.query(Student).filter(Student.name == stu_name).first()
        return result

    @staticmethod
    def add_dept(department_name):
        result = Department(name=department_name)
        return result

    @staticmethod
    def check(student):
        s = student.deparment.name
        return s

    @staticmethod
    def getdept(id, session):
        res = session.query(Department).filter(Department.id == id).first()
        return res

    @staticmethod
    def delete_d(department_D, session):
        session.delete(department_D)
        session.commit()
