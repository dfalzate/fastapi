from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
  name: str
  surname: str
  url: str
  age: int

class UserData(BaseModel):
  name: Optional[str] = None
  surname: Optional[str] = None
  url: Optional[str] = None
  age: Optional[int] = None