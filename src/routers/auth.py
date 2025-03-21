from fastapi import APIRouter, Depends, HTTPException

from tools.auth import verify, create_token, decode_token
from .users import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix='/auth')

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

class UserDB(User):
  password:str
  enabled:bool
  email:str
  
usersDB = [
  UserDB(
    id=1,
    email='email1@email.com',
    name='Name1',
    surname='SureName1',
    url='url1',
    age=1,
    enabled=True,
    password='$2a$10$CuiY7PYiHA1fJdJu8NZJ8eGzx8D7nZReiqG7i7XIznm.khaoPyQIG'
  ),
  UserDB(
    id=2,
    email='email2@email.com',
    name='Name2',
    surname='SureName2',
    url='url2',
    age=2,
    enabled=True,
    password='$2a$10$TyXMhQiEWaM1Z2Hzla6Tv.HLYPmDKABMm/2e/HnD2qgcUnF2n3cm2'
  )
]

async def getUser(email:str):
  user = filter(lambda user: user.email==email, usersDB)
  user_list = list(user)
  if not user_list:
    return None
  return user_list[0]

async def get_current_user(token:str=Depends(oauth2)):
  user= decode_token(token)
  if not user:
    raise HTTPException(status_code=400, detail='Incorrect email or password')
  return user 

@router.post('/login')
async def login(form_data:OAuth2PasswordRequestForm=Depends()):
  user = await getUser(form_data.username)
  if not user:
    raise HTTPException(status_code=400, detail='Incorrect email or password')
  if not verify(form_data.password, user.password):
    raise HTTPException(status_code=400, detail='Incorrect email or password')
  
  return {'access_token':create_token(user.model_dump(exclude={"password"})), 'token_type':'bearer'}

@router.get('/me')
async def me(user:User=Depends(get_current_user)):
  return user