from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    unit_price = Column(Float)
    sale_date = Column(Date)
