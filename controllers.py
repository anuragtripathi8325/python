from database import SessionLocal
from models import User, Department, Course, Branch, Teacher
from passlib.context import CryptContext
from auth import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def register_user(data):
    db = SessionLocal()

    try:
        existing_user = db.query(User).filter(User.email == data.email).first()
        if existing_user:
            return {
                "success": False,
                "message": "Email already registered"
            }

        hashed_password = pwd_context.hash(data.password)

        user = User(
            name=data.name,
            email=data.email,
            password=hashed_password,
            role=data.role
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "success": True,
            "message": "User registered successfully",
            "user_id": user.id,
            "role": user.role
        }

    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": "User registration failed",
            "error": str(e)
        }

    finally:
        db.close()


def register_bulk_users(data):
    db = SessionLocal()
    results = []
    success_count = 0
    failed_count = 0

    try:
        for user_data in data.users:
            existing_user = db.query(User).filter(User.email == user_data.email).first()

            if existing_user:
                results.append({
                    "email": user_data.email,
                    "success": False,
                    "message": "Email already registered"
                })
                failed_count += 1
                continue

            try:
                hashed_password = pwd_context.hash(user_data.password)
                user = User(
                    name=user_data.name,
                    email=user_data.email,
                    password=hashed_password,
                    role=user_data.role
                )
                db.add(user)
                db.commit()
                db.refresh(user)

                results.append({
                    "email": user_data.email,
                    "success": True,
                    "user_id": user.id,
                    "role": user.role
                })
                success_count += 1

            except Exception as e:
                db.rollback()
                results.append({
                    "email": user_data.email,
                    "success": False,
                    "message": str(e)
                })
                failed_count += 1

        return {
            "success": True,
            "message": f"{success_count} users registered, {failed_count} failed",
            "results": results
        }

    finally:
        db.close()


def login_user(data):
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.email == data.email).first()

        if not user:
            return {
                "success": False,
                "message": "Invalid email or password"
            }

        if not pwd_context.verify(data.password, user.password):
            return {
                "success": False,
                "message": "Invalid email or password"
            }

        token = create_access_token(data={
            "user_id": user.id,
            "email": user.email,
            "role": user.role
        })

        return {
            "success": True,
            "message": "Login successful",
            "access_token": token,
            "token_type": "bearer"
        }

    finally:
        db.close()


def create_department(data):
    db = SessionLocal()

    try:
        existing_department = db.query(Department).filter(Department.department_name == data.department_name).first()

        if existing_department:
            return {
                "success": False,
                "message": "Department already exists"
            }

        department = Department(
            department_name=data.department_name
        )

        db.add(department)
        db.commit()
        db.refresh(department)

        return {
            "success": True,
            "message": "Department created successfully",
            "department_id": department.id,
            "department_name": department.department_name
        }

    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": "Department creation failed",
            "error": str(e)
        }

    finally:
        db.close()


def get_all_departments():
    db = SessionLocal()

    try:
        departments = db.query(Department).all()

        result = []
        for dept in departments:
            result.append({
                "id": dept.id,
                "department_name": dept.department_name
            })

        return {
            "success": True,
            "departments": result
        }

    finally:
        db.close()


def create_course(data):
    db = SessionLocal()

    try:
        existing_department = db.query(Department).filter(Department.id == data.department_id).first()

        if not existing_department:
            return {
                "success": False,
                "message": "Department not found"
            }

        existing_course = db.query(Course).filter(Course.course_code == data.course_code).first()

        if existing_course:
            return {
                "success": False,
                "message": "Course code already exists"
            }

        course = Course(
            course_name=data.course_name,
            course_code=data.course_code,
            duration_years=data.duration_years,
            total_seats=data.total_seats,
            department_id=data.department_id
        )

        db.add(course)
        db.commit()
        db.refresh(course)

        return {
            "success": True,
            "message": "Course created successfully",
            "course_id": course.id,
            "course_name": course.course_name
        }

    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": "Course creation failed",
            "error": str(e)
        }

    finally:
        db.close()


def get_all_courses():
    db = SessionLocal()

    try:
        courses = db.query(Course).all()

        result = []
        for course in courses:
            result.append({
                "id": course.id,
                "course_name": course.course_name,
                "course_code": course.course_code,
                "duration_years": course.duration_years,
                "total_seats": course.total_seats,
                "department_id": course.department_id
            })

        return {
            "success": True,
            "courses": result
        }

    finally:
        db.close()


def create_branch(data):
    db = SessionLocal()

    try:
        existing_course = db.query(Course).filter(Course.id == data.course_id).first()

        if not existing_course:
            return {
                "success": False,
                "message": "Course not found"
            }

        existing_branch = db.query(Branch).filter(Branch.branch_code == data.branch_code).first()

        if existing_branch:
            return {
                "success": False,
                "message": "Branch code already exists"
            }

        branch = Branch(
            branch_name=data.branch_name,
            branch_code=data.branch_code,
            total_seats=data.total_seats,
            course_id=data.course_id
        )

        db.add(branch)
        db.commit()
        db.refresh(branch)

        return {
            "success": True,
            "message": "Branch created successfully",
            "branch_id": branch.id,
            "branch_name": branch.branch_name
        }

    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": "Branch creation failed",
            "error": str(e)
        }

    finally:
        db.close()


def get_all_branches():
    db = SessionLocal()

    try:
        branches = db.query(Branch).all()

        result = []
        for branch in branches:
            result.append({
                "id": branch.id,
                "branch_name": branch.branch_name,
                "branch_code": branch.branch_code,
                "total_seats": branch.total_seats,
                "course_id": branch.course_id
            })

        return {
            "success": True,
            "branches": result
        }

    finally:
        db.close()


def create_teacher(data):
    db = SessionLocal()

    try:
        existing_user = db.query(User).filter(User.id == data.user_id).first()

        if not existing_user:
            return {
                "success": False,
                "message": "User not found"
            }

        existing_department = db.query(Department).filter(Department.id == data.department_id).first()

        if not existing_department:
            return {
                "success": False,
                "message": "Department not found"
            }

        existing_teacher = db.query(Teacher).filter(Teacher.user_id == data.user_id).first()

        if existing_teacher:
            return {
                "success": False,
                "message": "Teacher profile already exists for this user"
            }

        existing_employee_id = db.query(Teacher).filter(Teacher.employee_id == data.employee_id).first()

        if existing_employee_id:
            return {
                "success": False,
                "message": "Employee ID already exists"
            }

        teacher = Teacher(
            user_id=data.user_id,
            employee_id=data.employee_id,
            department_id=data.department_id,
            designation=data.designation,
            qualification=data.qualification,
            phone_number=data.phone_number
        )

        db.add(teacher)
        db.commit()
        db.refresh(teacher)

        return {
            "success": True,
            "message": "Teacher profile created successfully",
            "teacher_id": teacher.id,
            "employee_id": teacher.employee_id
        }

    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": "Teacher creation failed",
            "error": str(e)
        }

    finally:
        db.close()


def get_all_teachers():
    db = SessionLocal()

    try:
        teachers = db.query(Teacher).all()

        result = []
        for teacher in teachers:
            result.append({
                "id": teacher.id,
                "user_id": teacher.user_id,
                "employee_id": teacher.employee_id,
                "department_id": teacher.department_id,
                "designation": teacher.designation,
                "qualification": teacher.qualification,
                "phone_number": teacher.phone_number
            })

        return {
            "success": True,
            "teachers": result
        }

    finally:
        db.close()