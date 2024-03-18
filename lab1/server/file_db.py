from datetime import time, date
from sqlalchemy import create_engine, VARCHAR, Column, Float, Date, Time
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column


def create_custom_session(server: str, server_login: str, password: str, db_name: str, table_name: str):
    if table_name != "file_contents":
        return False
    url = server + "://" + server_login + ":" + password + "@localhost:5432/" + db_name
    engine = create_engine(url)
    with Session(engine) as session:
        yield session


class Base(DeclarativeBase):
    pass


class FileContent(Base):
    __tablename__ = "file_contents"

    create_date: Mapped[date] = mapped_column(Date, primary_key=True)
    create_time: Mapped[time] = mapped_column(Time, primary_key=True)
    var1: Mapped[float] = mapped_column(Float)
    var2: Mapped[float] = mapped_column(Float)
    var3: Mapped[float] = mapped_column(Float)
    var4: Mapped[float] = mapped_column(Float)
