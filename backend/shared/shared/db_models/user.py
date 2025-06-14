from shared.db_models.base import BaseUser
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, UTC

class User(BaseUser):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    registered_date = Column(DateTime(timezone=True), default=datetime.now(UTC))
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
