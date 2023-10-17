from project.app.models.student import Student
from project.app.models.Department import Department
from project.app.models.Teacher import Teacher
from project.app.models.Course import Course
from project.app.models.Designation import Designation
from project.app.db import db


class StudentRepository:
    @staticmethod
    def add_student(args):
        student = Student(
            name=args.get("name"),
            address=args.get("address"),
            email=args.get("email"),
            number=args.get("number"),
        )
        res1 = Designation(
            designation_id=args["designation"]["designation_id"],
            name=args["designation"]["name"],
        )
        student.designation.append(res1)
        db.session.add(student)
        db.session.add(res1)
        db.session.commit()
        # return res

    @staticmethod
    def get_student(id, session):
        result = session.query(Student).filter(Student.id == id)

        return result.first()

    @staticmethod
    def student_update_q(student, student_data):
        for key, value in student_data.items():
            setattr(student, key, value)

        db.session.commit()

    def student_update_q2(student, student_data):
        student.name = student_data.get("name")
        student.email = student_data.get("email")
        student.address = student_data.get("address")
        student.number = student_data.get("number")
        db.session.commit()  # added

    @staticmethod
    def get_all_student_q():
        result = Student.query.all()
        return result

    @staticmethod
    def delete_commit(student_D, session):
        session.delete(student_D)
        session.commit()

    @staticmethod
    def searched(session, se):
        # results_table1 = (
        #     session.query(Department.name).filter(Department.name.like(f"%{se}%")).all()
        # )
        # results_table2 = (
        #     session.query(Student.name).filter(Student.name.like(f"%{se}%")).all()
        # )
        combined_query = (
            session.query(Department.name)
            .filter(Department.name.like(f"%{se}%"))
            .union(session.query(Student.name).filter(Student.name.like(f"%{se}%")))
            .union(session.query(Course.name).filter(Course.name.like(f"%{se}%")))
        )

        # Execute the combined query

        return combined_query.all()
