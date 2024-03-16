from fastapi import FastAPI, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel
from starlette.responses import Response

from db import get_session, User

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


class SQLConnectData(BaseModel):
    server = str
    login = str
    password = str
    db_name = str
    table_name = str

#class File ???????

@app.post('/upload', status_code=status.HTTP_200_OK)
def upload_file(file: UploadFile):
    print(file.file.read())
    return file.filename


@app.post("/register")
def register(data: LoginData, session: Session = Depends(get_session)):
    existing = session.execute(select(User).where(User.username == data.login)).first()
    if existing is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    user: User = User(username=data.login, user_password=data.password)
    session.add(user)
    session.commit()
    return user


@app.post("/login")
def login(data: LoginData, session: Session = Depends(get_session)):
    existing = session.execute(select(User).where(User.username == data.login)).first()[0]
    if existing is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if existing.user_password != data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return Response(status_code=status.HTTP_200_OK)