from fastapi import FastAPI

from app.core.database import engine, Base
from app.models import sale

from app.routers import sales_router, analytics_router

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sales Analytics API",
    description="""
API REST para **registro e análise de vendas**.

### Funcionalidades
- Cadastro de vendas
- Métricas de negócio automatizadas
- Análises com Pandas

Projeto desenvolvido com foco em **arquitetura backend e dados**.
""",
    version="1.0.0",
    contact={
        "name": "Felipe Thiago",
        "url": "https://github.com/felipethiago21"
    }
)


# Routers
app.include_router(
    sales_router.router,
    prefix="/sales",
    tags=["Sales"]
)

app.include_router(
    analytics_router.router,
    prefix="/analytics",
    tags=["Analytics"]
)

@app.get("/", tags=["Health"])
def root():
    return {"status": "API rodando com sucesso"}

