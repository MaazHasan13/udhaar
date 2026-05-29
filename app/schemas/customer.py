from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    phone: str
    address: str

class CustomerUpdate(BaseModel):
    name: str
    phone: str
    address: str