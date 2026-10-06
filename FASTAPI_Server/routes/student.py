from fastapi import APIRouter
student_router=APIRouter(prefix="/student")
#localhost:8000/student/addstudent
@student_router.post("/addStudent")
def addStudent():
    return "add student method called"
#localhost:8000/student/getstudent
@student_router.get("/getStudent")
def getStudent():
    return "get student method called"
#localhost:8000/student/updateStudent =>put
@student_router.put("/updatestudent")
def putStudent():
    return "update student method called"
#localhost:8000/student/updateStudent => delete
@student_router.delete("/deletestudent")
def deleteStudent():
        return "delete student method called"
    


