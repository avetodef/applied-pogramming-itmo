from fastapi import FastAPI, UploadFile, Depends, HTTPException, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, HTMLResponse
from fastapi.templating import Jinja2Templates
import csv
import codecs

from db import get_session, User, FileContent
from file_db import create_custom_session

app = FastAPI()
templates = Jinja2Templates(directory="templates")

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


class Base(BaseModel):
    server: str
    login: str
    password: str
    db_name: str
    table_name: str


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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


#СУКА КАК ЭТО ДЕЛАТЬ Я НЕ ПОНИМАЮ НАХ
@app.post('/upload')
def upload_file(server: str, server_login: str, password: str, db_name: str, table_name: str, file: UploadFile, Session = Depends(get_session)):
    url = server + "://" + server_login + ":" + password + "@localhost:5432/" + db_name
    DATABASE = "postgresql://postgres:lterm54201@localhost:5432/applied_prog_lab_1"
    print(url)
    print(DATABASE)
    if url != DATABASE:
        print("WTF")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    # Session = Depends(create_custom_session(server, server_login, password, db_name, table_name))
    # if not Session:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    print(csvToJSON(file))

    return Response(status_code=status.HTTP_200_OK)


def csvToJSON(file):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data = {}
    for rows in csvReader:
        key = rows['create_date', 'create_time']
        data[key] = rows

    file.file.close()
    return data
