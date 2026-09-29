from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = "student"


class BulkUserCreate(BaseModel):
    users: List[UserCreate]


class LoginRequest(BaseModel):
    email: str
    password: str


class DepartmentCreate(BaseModel):
    department_name: str


class CourseCreate(BaseModel):
    course_name: str
    course_code: str
    duration_years: int
    total_seats: int
    department_id: int


class BranchCreate(BaseModel):
    branch_name: str
    branch_code: str
    total_seats: int
    course_id: int


class TeacherCreate(BaseModel):
    user_id: int
    employee_id: str
    department_id: int
    designation: str
    qualification: str
    phone_number: str