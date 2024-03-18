from sqlalchemy import create_engine,  String , Float, Date, Time
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from datetime import time, date

DATABASE_URL = "postgresql://postgres:lterm54201@localhost:5432/applied_prog_lab_1"
engine = create_engine(DATABASE_URL)



def get_session():
    with Session(engine) as session:
        yield session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), primary_key=True)
    user_password: Mapped[str] = mapped_column(String(50))


class FileContent(Base):
    __tablename__ = "file_contents"

    create_date: Mapped[date] = mapped_column(Date, primary_key=True)
    create_time: Mapped[time] = mapped_column(Time, primary_key=True)
    var1: Mapped[float] = mapped_column(Float)
    var2: Mapped[float] = mapped_column(Float)
    var3: Mapped[float] = mapped_column(Float)
    var4: Mapped[float] = mapped_column(Float)


