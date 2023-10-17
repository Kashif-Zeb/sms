from project.app.models.Course import Course
from project.app.db import db
from project.app.models.File import File
from project.app.models.student import Student


class CourseRepository:
    @staticmethod
    def get_course_name(session, course_name):
        result = session.query(Course).filter(Course.name == course_name).first()
        return result

    @staticmethod
    def add_new_course(course_name):
        ci = Course(name=course_name)
        return ci

    @staticmethod
    def add_file_db(filename, file_path):
        newFile = File(filename=filename, path=file_path)
        db.session.add(newFile)
        db.session.commit()

    @staticmethod
    def get_file(filename, session):
        # breakpoint()
        file_record = session.query(File).filter(File.filename == filename).first()
        return file_record.filename
