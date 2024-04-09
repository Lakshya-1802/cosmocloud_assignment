from fastapi import FastAPI
# from routes.studentroutes import router  # Import the router from studentroutes.py

app = FastAPI()

# Include the student router
# app.include_router(router)

@app.get('/')
def root():
    return {'message': 'App Running'}

# @app.post('/create')
# def create(data: modals.Todo): 
#     id = db.create(data)  
#     return {'inserted': True, 'id': id}

# @app.get('/get/all')
# def get_all():
#     data = db.get_all()
#     return {'data': data}

# # @app.get('/get/{name}') for path parameter
# @app.get('/get') #dor query parameter don pass anything in path
# def get(name:str):
#     data = db.get(name)
#     return {'data': data}

# @app.delete('/delete')
# def delete(name:str):
#     data=db.delete(name)
#     return {'Message': 'Deleted Succesfully','Deleted Count':data}

# @app.put('/update')
# def update(data: modals.Todo):
#     data=db.update(data)
#     return {'Message': data}