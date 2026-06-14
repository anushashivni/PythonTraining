from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello"}

student =[]

class Student(BaseModel):
    name:str
    age:int 

@app.post("/students/")
def create_student(studentclass:Student):
    student.append(studentclass.dict())
    return student  

@app.get("/")
def getStudents():
    return student


@app.put("/students/{name}")
def update_Student(name:str, studentclass:Student):
    for item in student:
        if item.name == name:
            return Student
