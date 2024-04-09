from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    city: str | None = None
    country: str | None = None

class Student(BaseModel):
    name: str | None = None
    age: int | None = None
    address: Address

class UpdateAddress(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: UpdateAddress
