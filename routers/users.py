from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])

class User(BaseModel):
  id: int
  name: str
  surname: str
  url: str
  age: int

class UserData(BaseModel):
  name: Optional[str] = None
  surname: Optional[str] = None
  url: Optional[str] = None
  age: Optional[int] = None

users = [
  User(
    id=1,
    name="Name1",
    surname="SureName1",
    url="url1",
    age=1
  ),
  User(
    id=2,
    name="Name2",
    surname="SureName2",
    url="url2",
    age=2
  ),
  User(
    id=3,
    name="Name3",
    surname="SureName3",
    url="url3",
    age=3
  ),
  User(
    id=4,
    name="Name4",
    surname="SureName4",
    url="url4",
    age=4
  )
]

@router.get("/", response_model=List[User])
async def getUsers():
  return users

@router.get("/{userId}", response_model=User)
async def getUser(userId:int):
  try:
    user = filter(lambda user: user.id==userId, users)
    user_list = list(user)
    if not user_list:
      raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user_list[0]
  except HTTPException:
    raise

@router.get("/query")
async def getUserQuery(id:int):
  try:
    user = filter(lambda user: user.id==id, users)
    return list(user)[0]
  except:
    return {"error":"No se ha encontrado el usuario"}

@router.post("/", response_model=User)
async def createUser(user:User):
  try:
    users.append(user)
    return user
  except:
    return {"error":"No se ha encontrado el usuario"}

@router.put("/{userId}", response_model=User)
async def updateUser(userId:int, userData:UserData):
  try:
    print(userId)
    print(userData)
  except:
    return {"error":"Error message"}
  
@router.delete("/{userId}")
async def deleteUser(userId:int):
  for index, user in enumerate(users):
    if user.id==userId:
      del users[index]
      raise HTTPException(status_code=200, detail="Usuario borrado")
    
  raise HTTPException(status_code=404, detail="Usuario no encontrado")