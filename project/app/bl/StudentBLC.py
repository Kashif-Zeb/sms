from flask_jwt_extended import create_access_token
from project.app.repositories.StudentRepository import StudentRepository
from project.app.repositories.userrepository import UsersRepository
from project.app.db import db
from flask import request, jsonify
from project.app.models.Users import Users
from werkzeug.security import generate_password_hash, check_password_hash


class StudentBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_student_desig(args):
        # breakpoint()
        res = StudentRepository.add_student(args)
        return res

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

    @staticmethod
    def registering(email, password):
        session = StudentBLC.get_session()
        if not email or not password:
            return jsonify({"message": "Username and password are required"}), 400
        if email:
            UsersRepository.get_emal_user(session, email)
            return jsonify({"message": "Username already exists"}), 400

        # Store the hashed password in the database
        hu = UsersRepository.add_user(password, email)
        return jsonify({"message": "Registration successful"}), 201

    @staticmethod
    def loging(email, password):
        session = StudentBLC.get_session()
        if not email or not password:
            return jsonify({"message": "Username and password are required"}), 400
        user = UsersRepository.checking(session, email)
        if user is not None and check_password_hash(user.passwords, password):
            return jsonify({"message": "Invalid credentials"}), 401

        # Create an access token
        access_token = create_access_token(identity=email)
        return jsonify({"access_token": f"Bearer {access_token}"}), 200
