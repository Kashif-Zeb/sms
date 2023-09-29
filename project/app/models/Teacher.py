from project.app.db import db
from project.app.models.student import foriegnkey


class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    student = db.relationship(
        "Student",
        secondary=foriegnkey.student_teacher,
        back_populates="teacher",
    )
    department = db.relationship(
        "Department",
        secondary=foriegnkey.teacher_department,
        back_populates="teacher",
    )
