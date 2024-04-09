from fastapi import APIRouter
from models.studentModels import Student

router = APIRouter()

@router.post("/students")
async def create_student(student: Student):
    return {"name": student.name, "age": student.age, "address": student.address.dict()}
