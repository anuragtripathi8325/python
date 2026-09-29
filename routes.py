from fastapi import APIRouter, Depends

from controllers import (
    register_user, register_bulk_users, login_user,
    create_department, get_all_departments,
    create_course, get_all_courses,
    create_branch, get_all_branches,
    create_teacher, get_all_teachers
)
from schemas import (
    UserCreate, BulkUserCreate, LoginRequest,
    DepartmentCreate, CourseCreate, BranchCreate, TeacherCreate
)
from auth import get_current_user, require_role

router = APIRouter()


@router.post("/register", tags=["Auth"])
def register(data: UserCreate):
    return register_user(data)


@router.post("/register-bulk", tags=["Auth"])
def register_bulk(data: BulkUserCreate):
    return register_bulk_users(data)


@router.post("/login", tags=["Auth"])
def login(data: LoginRequest):
    return login_user(data)


@router.get("/me", tags=["Auth"])
def get_my_profile(current_user: dict = Depends(get_current_user)):
    return {
        "success": True,
        "message": "Token verified successfully",
        "user": current_user
    }


@router.post("/departments", tags=["Department"])
def add_department(data: DepartmentCreate, current_user: dict = Depends(require_role(["admin"]))):
    return create_department(data)


@router.get("/departments", tags=["Department"])
def list_departments():
    return get_all_departments()


@router.post("/courses", tags=["Course"])
def add_course(data: CourseCreate, current_user: dict = Depends(require_role(["admin"]))):
    return create_course(data)


@router.get("/courses", tags=["Course"])
def list_courses():
    return get_all_courses()


@router.post("/branches", tags=["Branch"])
def add_branch(data: BranchCreate, current_user: dict = Depends(require_role(["admin"]))):
    return create_branch(data)


@router.get("/branches", tags=["Branch"])
def list_branches():
    return get_all_branches()


@router.post("/teachers", tags=["Teacher"])
def add_teacher(data: TeacherCreate, current_user: dict = Depends(require_role(["admin"]))):
    return create_teacher(data)


@router.get("/teachers", tags=["Teacher"])
def list_teachers(current_user: dict = Depends(require_role(["admin", "teacher"]))):
    return get_all_teachers()