from fastapi import FastAPI, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel

from .db import get_session, User

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginData(BaseModel):
    login: str
    password: str


@app.post('/upload', status_code=status.HTTP_200_OK)
def upload_file(file: UploadFile):
    print(file.file.read())
    return file.filename


@app.post('/login', status_code=status.HTTP_200_OK)
def login(data: LoginData) -> LoginData:
    print(data.login, data.password)
    return data


@app.get("/users")
def example(session: Session = Depends(get_session)):
    return session.execute(select(User)).all()