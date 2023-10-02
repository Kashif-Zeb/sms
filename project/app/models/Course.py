from project.app.db import db
from project.app.models.student import foriegnkey


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    department = db.relationship(
        "Department", secondary=foriegnkey.course_department, back_populates="course"
    )
