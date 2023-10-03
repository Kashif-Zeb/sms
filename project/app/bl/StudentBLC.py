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
    def updating_student2(id, student_data):
        # breakpoint()
        # data = request.get_json()
        session = StudentBLC.get_session()
        student = StudentRepository.get_student(id, session)
        if not student:
            return jsonify({"message": f"student {id} not found"})
        up = StudentRepository.student_update_q2(student, student_data)
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

    @staticmethod
    def searching(se):
        session = StudentBLC.get_session()
        # breakpoint()
        results = StudentRepository.searched(session, se)

        # matching_names_table1 = [result.name for result in results_table1]
        # matching_names_table2 = [result.name for result in results_table2]

        # Combine matching names from both tables if needed
        # matching_names = matching_names_table1 + matching_names_table2
        matching_names = [{"name": result[0]} for result in results]
        name_values = [item["name"] for item in matching_names]
        return name_values
