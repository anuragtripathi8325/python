from fastapi import FastAPI
from sqlalchemy import text

from routes import router
from database import engine, Base

import models


app = FastAPI()

# Automatically create tables
Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Student Result Management API is running"
    }


@app.get("/test-db")
def test_database():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            value = result.scalar()

            print("================================")
            print("MYSQL CONNECTION: SUCCESS")
            print("Database:", connection.engine.url.database)
            print("SELECT 1 result:", value)
            print("================================")

            return {
                "status": "success",
                "message": "MySQL connected successfully",
                "database": connection.engine.url.database,
                "select_1": value
            }

    except Exception as e:
        print("================================")
        print("MYSQL CONNECTION: FAILED")
        print("Error:", e)
        print("================================")

        return {
            "status": "error",
            "message": "MySQL connection failed",
            "error": str(e)
        }