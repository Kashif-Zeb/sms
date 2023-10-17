from project.app.db import db
from project.app.models.student import foriegnkey


class Designation(db.Model):
    __tablename__ = "designation"
    id = db.Column(db.Integer, primary_key=True)
    designation_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    student = db.relationship(
        "Student",
        secondary=foriegnkey.student_designation,
        back_populates="designation",
    )
