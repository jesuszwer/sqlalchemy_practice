from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr
from model import RoleEnum

class UsersAddDTO(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: RoleEnum
    
class UsersDTO(UsersAddDTO):
    id: int