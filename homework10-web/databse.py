import hashlib

from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///users.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    user = Column(String)


Base.metadata.create_all(bind=engine)


def crypt(password):
    md51 = hashlib.md5()
    md51.update(password.encode("utf-8"))
    hash_1 = md51.hexdigest()
    return hash_1


def put_data_in_table(email: str, password: str, user: str):
    s = SessionLocal()
    password = crypt(password)
    user = User(
        email=email,
        password=password,
        user=user,
    )
    s.add(user)
    s.commit()


def check_password():
    s = SessionLocal()
    password_in_table = s.query(User.password).all()
    pass1 = password_in_table[1]
    pass2 = password_in_table[0]
    if pass1 == pass2:
        pass
    else:
        pass
