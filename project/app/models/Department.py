from project.app.db import db
from project.app.models.student import foriegnkey


class Department(db.Model):
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    student = db.relationship(
        "Student",
        secondary=foriegnkey.student_department,
        back_populates="department",
    )
    teacher = db.relationship(
        "Teacher",
        secondary=foriegnkey.teacher_department,
        back_populates="department",
    )
    courses = db.relationship(
        "Course", secondary=foriegnkey.course_department, back_populates="department"
    )
