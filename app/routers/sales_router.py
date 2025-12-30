from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.sale import Sale
from app.schemas.sale_schema import SaleCreate, SaleResponse

router = APIRouter()

@router.post("/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = Sale(
        product_name=sale.product_name,
        quantity=sale.quantity,
        unit_price=sale.unit_price,
        sale_date=sale.sale_date
    )
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale
