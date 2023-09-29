from project.app.repositories.StudentRepository import StudentRepository
from project.app.db import db
from flask import request, jsonify


class StudentBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def get_student(id):
        session = StudentBLC.get_session()
        student = StudentRepository.get_student(id, session)
        if not student:
            raise Exception({"message": f"{id} not found"})

        return student

    @staticmethod
    def updating_student(id, student_data):
        # breakpoint()
        # data = request.get_json()
        session = StudentBLC.get_session()
        student = StudentRepository.get_student(id, session)
        if not student:
            return jsonify({"message": f"student {id} not found"})
        up = StudentRepository.student_update_q(student, student_data)
        return up

    @staticmethod
    def get_student_data(id):
        session = StudentBLC.get_session()
        student = StudentRepository.get_student(id, session)
        if not student:
            return jsonify({"message": "student not found"})

        return student

    @staticmethod
    def delete_student(id):
        session = StudentBLC.get_session()
        student_D = StudentRepository.get_student(id, session)
        if not student_D:
            return jsonify({"message": f"student {id} not found"})
        else:
            StudentRepository.delete_commit(student_D, session)
