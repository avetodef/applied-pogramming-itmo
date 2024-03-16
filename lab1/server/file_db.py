from sqlalchemy import create_engine, VARCHAR, Column, String
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

DATABASE_URL = "postgresql://postgres:lterm54201@localhost:5432/applied_prog_lab_1"
engine = create_engine(DATABASE_URL)



def get_session():
    with Session(engine) as session:
        yield session


class Base(DeclarativeBase):
    pass


class FileContent(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), primary_key=True)
    user_password: Mapped[str] = mapped_column(String(50))