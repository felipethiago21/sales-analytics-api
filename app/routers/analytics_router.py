from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.analytics_service import (
    summary_metrics,
    monthly_sales,
    top_products
)

router = APIRouter()


@router.get(
    "/summary",
    summary="Resumo geral de vendas",
    description=(
        "Retorna métricas consolidadas de vendas, incluindo "
        "faturamento total, ticket médio e total de registros."
    )
)
def get_summary(db: Session = Depends(get_db)):
    return summary_metrics(db)


@router.get(
    "/monthly",
    summary="Vendas agrupadas por mês",
    description=(
        "Retorna o faturamento total agrupado por mês, "
        "útil para análises de crescimento e sazonalidade."
    )
)
def get_monthly(db: Session = Depends(get_db)):
    return monthly_sales(db)


@router.get(
    "/top-products",
    summary="Produtos mais vendidos",
    description=(
        "Lista os produtos com maior faturamento total, "
        "ordenados do maior para o menor."
    )
)
def get_top_products(
    limit: int = Query(5, ge=1, le=20, description="Quantidade de produtos retornados"),
    db: Session = Depends(get_db)
):
    return top_products(db, limit)
