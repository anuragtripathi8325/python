from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    role = Column(String(20), default="student")


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    department_name = Column(String(100), unique=True)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_name = Column(String(100))
    course_code = Column(String(20))
    duration_years = Column(Integer)
    total_seats = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True)
    branch_name = Column(String(100))
    branch_code = Column(String(20))
    total_seats = Column(Integer)
    course_id = Column(Integer, ForeignKey("courses.id"))


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    employee_id = Column(String(30), unique=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    designation = Column(String(50))
    qualification = Column(String(100))
    phone_number = Column(String(15))