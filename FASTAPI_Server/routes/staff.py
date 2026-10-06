from fastapi import APIRouter
staff_router=APIRouter(prefix="/staff")
#localhost:8000/student/addstaff
@staff_router.post("/addstaff")
def addstaff():
    return "add staff method called"
#localhost:8000/student/getstaff
@staff_router.get("/getstaff")
def getstaff():
    return "get staff method called"
#localhost:8000/staff/updatestaff =>put
@staff_router.put("/updatstaff")
def pustaff():
    return "update staff method called"
#localhost:8000/staff/updatestaff => delete
@staff_router.delete("/deletestaff")
def deletestaff():
        return "delete staff method called"
    


