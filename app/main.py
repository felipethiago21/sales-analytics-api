from fastapi import FastAPI

from app.core.database import engine, Base
from app.models import sale

from app.routers import sales_router, analytics_router

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sales Analytics API",
    description="API para análise de vendas",
    version="1.0.0"
)

# Routers
app.include_router(sales_router.router, prefix="/sales", tags=["Sales"])
app.include_router(analytics_router.router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
def root():
    return {"status": "API rodando com sucesso"}
