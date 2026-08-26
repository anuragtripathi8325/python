from database import SessionLocal
from models import User


def register_user(data):
    db = SessionLocal()

    try:
        user = User(
            name=data.name,
            email=data.email,
            password=data.password
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "success": True,
            "message": "User registered successfully",
            "user_id": user.id
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