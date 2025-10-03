from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class AnswerCreate(BaseModel):
    question: str
    answer: str

class AnswerOut(BaseModel):
    id: int
    question: str
    answer: str
    score: float
    timestamp: datetime

    class Config:
        orm_mode = True
