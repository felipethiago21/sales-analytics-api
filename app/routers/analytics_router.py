from fastapi import APIRouter

router = APIRouter()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.analytics_service import (
    summary_metrics,
    monthly_sales,
    top_products
)

router = APIRouter()

@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    return summary_metrics(db)


@router.get("/monthly")
def get_monthly(db: Session = Depends(get_db)):
    return monthly_sales(db)


@router.get("/top-products")
def get_top_products(db: Session = Depends(get_db)):
    return top_products(db)
