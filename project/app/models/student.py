from project.app.db import db


class foriegnkey:
    student_department = db.Table(
        "student_department",
        db.Column(
            "student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True
        ),
        db.Column(
            "department_id",
            db.Integer,
            db.ForeignKey("department.id"),
            primary_key=True,
        ),
        # db.Column("teacher_id", db.Integer, db.ForeignKey("teacher.id"), primary_key=True),
    )

    student_teacher = db.Table(
        "student_teacher",
        db.Column(
            "student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True
        ),
        db.Column(
            "teacher_id", db.Integer, db.ForeignKey("teacher.id"), primary_key=True
        ),
    )

    teacher_department = db.Table(
        "teacher_department",
        db.Column(
            "teacher_id", db.Integer, db.ForeignKey("teacher.id"), primary_key=True
        ),
        db.Column(
            "department_id",
            db.Integer,
            db.ForeignKey("department.id"),
            primary_key=True,
        ),
    )
    course_department = db.Table(
        "course_department",
        db.Column(
            "course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True
        ),
        db.Column(
            "department_id",
            db.Integer,
            db.ForeignKey("department.id"),
            primary_key=True,
        ),
    )
    student_designation = db.Table(
        "student_designation",
        db.Column(
            "student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True
        ),
        db.Column(
            "designation_id",
            db.Integer,
            db.ForeignKey("designation.id"),
            primary_key=True,
        ),
    )


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    address = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    number = db.Column(db.String(50), unique=True, nullable=False)
    department = db.relationship(
        "Department",
        secondary=foriegnkey.student_department,
        back_populates="student",
    )

    teacher = db.relationship(
        "Teacher",
        secondary=foriegnkey.student_teacher,
        back_populates="student",
    )
    designation = db.relationship(
        "Designation",
        secondary=foriegnkey.student_designation,
        back_populates="student",
    )
