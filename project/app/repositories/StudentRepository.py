from project.app.models.student import Student
from project.app.db import db


class StudentRepository:
    @staticmethod
    def add_student(student):
        db.session.add(student)
        db.session.commit()
        return student

    @staticmethod
    def get_student(id, session):
        result = session.query(Student).filter(Student.id == id)

        return result.first()

    @staticmethod
    def student_update_q(student, student_data):
        for key, value in student_data.items():
            setattr(student, key, value)

        db.session.commit()

    @staticmethod
    def get_all_student_q():
        result = Student.query.all()
        return result

    @staticmethod
    def delete_commit(student_D, session):
        session.delete(student_D)
        session.commit()
