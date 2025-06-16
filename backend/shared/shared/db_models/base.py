from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from shared.config import USERS_DATABASE_URL, AUTH_DATABASE_URL

engine_auth = create_engine(AUTH_DATABASE_URL, pool_size=10, max_overflow=5, pool_timeout=30, pool_recycle=1800, echo=True)
SessionAuth = sessionmaker(autocommit=False, autoflush=False, bind=engine_auth)

engine_user = create_engine(USERS_DATABASE_URL, pool_size=10, max_overflow=5, pool_timeout=30, pool_recycle=1800, echo=True)
SessionUsers = sessionmaker(autocommit=False, autoflush=False, bind=engine_user)

BaseUser = declarative_base()
BaseAuth = declarative_base()

def get_auth_db():
    db = SessionAuth()
    try:
        yield db
    finally:
        db.close()

def get_users_db():
    db = SessionUsers()
    try:
        yield db
    finally:
        db.close()
