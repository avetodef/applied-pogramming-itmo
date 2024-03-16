from fastapi import FastAPI, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, VARCHAR, Time, Date
from databases import Database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "postgresql://postgres:lterm54201@localhost:5432/applied_prog_lab_1"
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()


class User(Base):
    __tablename__ = "users"

    username = Column(VARCHAR,primary_key=True,nullable=False)
    user_password = Column(VARCHAR,nullable=False)


Base.metadata.create_all(bind=engine)


class LoginData(BaseModel):
    login: str
    password: str


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users/")
async def get_users():
    query = User.__table__.select()
    return await database.fetch_all(query)


@app.post('/upload', status_code=status.HTTP_200_OK)
def upload_file(file: UploadFile):
    print(file.file.read())
    return file.filename

@app.post('/login', status_code=status.HTTP_200_OK)
def login(data: LoginData) -> LoginData:
    print(data.login, data.password)
    return data

