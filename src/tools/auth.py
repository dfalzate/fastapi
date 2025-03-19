from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
import jwt
from jwt import PyJWTError as JWTError
from passlib.context import CryptContext
from config.config import SECRET_KEY 

algorithm = "HS256"
crypt = CryptContext(schemes=["bcrypt"])

def verify(password, hashed_password):
  return crypt.verify(password, hashed_password)

def create_token(data:dict):
  expire = datetime.now(timezone.utc) + timedelta(minutes=1)
  data["exp"] = expire
  return jwt.encode(
      data,
      *SECRET_KEY,
      algorithm=algorithm,
    )

def decode_token(token:str):
  print(token)
  try:
    return jwt.decode(token, *SECRET_KEY, algorithms=[algorithm])
  except JWTError:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token no valido')