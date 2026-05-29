from fastapi import APIRouter
from fastapi import Depends,HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    new_customer = Customer(
        name=customer.name,
        phone=customer.phone,
        address=customer.address
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return {
        "message": "Customer created successfully",
        "customer_id": new_customer.id
    }

@router.get("/")
def get_customers(
    db: Session = Depends(get_db)
):
    customers = db.query(Customer).all()

    return customers

@router.get("/")
def get_customers(
    db: Session = Depends(get_db)
):
    customers = db.query(Customer).all()

    return customers

@router.get("/{customer_id}")
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate
)
@router.put("/{customer_id}")
def update_customer(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session = Depends(get_db)
):

    existing_customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not existing_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    existing_customer.name = customer.name
    existing_customer.phone = customer.phone
    existing_customer.address = customer.address

    db.commit()
    db.refresh(existing_customer)

    return {
        "message": "Customer updated successfully"
    }

@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully"
    }