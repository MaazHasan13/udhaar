from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    phone = Column(String, nullable=False)

    address = Column(String, nullable=True)

from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    phone: str
    address: str