from fastapi import APIRouter, HTTPException, Query
from db import collection
from schemas.studentSchemas import all_students_entity, student_entity
from models.studentModels import Student,updateStudent
from bson.objectid import ObjectId

router = APIRouter()

@router.post('/students')
async def create_student(data: Student):
    try:
        resp = collection.insert_one(data.model_dump())
        return {'id': str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')

@router.get('/students')
async def all_students(country: str = Query(None), age: int = Query(None)):
    try:
        # Filter students based on country and age if provided
        filter_query = {}
        if country:
            filter_query['address.country'] = country
        if age:
            filter_query['age'] = {'$gte': age}

        # Retrieve data from the database based on the filter
        data = list(collection.find(filter_query))

        if not data:
            return {'status_code': 404, 'detail': 'Data Not found'}

        return all_students_entity(data)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')

@router.get('/students/{id}')
async def get_student_by_id(id: str):
    try:
        id = ObjectId(id)
        student = collection.find_one({'_id': id})
        if student:
            return student_entity(student)
        else:
            raise HTTPException(status_code=404, detail="Student not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')
    
    
@router.patch('/students/{id}')
async def update_student_by_id(id: str, updated_data: updateStudent):
    try:
        id = ObjectId(id)
        
        existing = collection.find_one({'_id': id})
        if not existing:
            raise HTTPException(status_code=404, detail="Student not found")
        
        update_fields = updated_data.model_dump(exclude_unset=True)

        resp = collection.update_one({'_id': id}, {'$set': update_fields})

        if resp.modified_count == 1:
            return {'message': 'Student updated successfully'}
        else:
            raise HTTPException(status_code=500, detail="Failed to update student")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')

@router.delete('/students/{id}')
async def delete_student_by_id(id: str):
    try:
        id = ObjectId(id)

        existing = collection.find_one({'_id': id})
        if not existing:
            raise HTTPException(status_code=404, detail="Student not found")

        result = collection.delete_one({'_id': id})
        
        if result.deleted_count == 1:
            return {}
        else:
            raise HTTPException(status_code=500, detail="Failed to delete student")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')
