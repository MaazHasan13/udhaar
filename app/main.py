from fastapi import FastAPI

from app.core.database import Base, engine

from app.models.user import User
from app.models.customer import Customer

from app.routers.auth import router as auth_router
from app.routers.customer import router as customer_router
from app.routers.product import router as product_router

app = FastAPI(title="UdhaarBook")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(customer_router)
app.include_router(product_router)

@app.get("/")
def home():
    return {
        "message": "UdhaarBook Running"
    }