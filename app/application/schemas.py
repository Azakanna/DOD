from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)


class ShowUser(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
