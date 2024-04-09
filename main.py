from fastapi import FastAPI
from routes.studentsRouter import router as student_router

app = FastAPI()

# Include student routes
app.include_router(student_router)

@app.get('/')
def root():
    return {'message': 'App is Running'}
