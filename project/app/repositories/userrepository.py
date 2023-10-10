from project.app.models.Users import Users
from project.app.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class UsersRepository:
    @staticmethod
    def get_emal_user(session, email):
        result = session.query(Users).filter(Users.email == email).first()
        return result

    @staticmethod
    def add_user(password, email):
        re = Users(passwords=generate_password_hash(password), email=email)
        return re

    @staticmethod
    def checking(session, email):
        em = session.query(Users).filter(Users.email == email).first()
        return em
