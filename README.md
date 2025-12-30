📊 Sales Analytics API

API REST desenvolvida em Python com FastAPI para registro e análise de vendas, aplicando boas práticas de arquitetura backend e processamento de dados.

O projeto permite cadastrar vendas, persistir dados em banco e gerar métricas de negócio automaticamente.

🚀 Funcionalidades

Cadastro de vendas via API

Persistência em banco de dados (SQLite)

Análise de dados com Pandas

Métricas de negócio:

Faturamento total

Ticket médio

Total de vendas

Vendas mensais

Produtos mais vendidos

Documentação automática com Swagger (OpenAPI)

🛠️ Stack Tecnológica

Python 3.11+

FastAPI

SQLAlchemy

Pandas

SQLite

Pydantic

Uvicorn

🧱 Arquitetura do Projeto
sales-analytics-api/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   └── database.py
│   ├── models/
│   │   └── sale.py
│   ├── schemas/
│   │   └── sale_schema.py
│   ├── services/
│   │   └── analytics_service.py
│   ├── routers/
│   │   ├── sales_router.py
│   │   └── analytics_router.py
│   └── utils/
│
├── tests/
├── requirements.txt
├── README.md
└── sales.db

🔌 Endpoints Disponíveis
📦 Sales

POST /sales – Cadastra uma venda

📊 Analytics

GET /analytics/summary – Resumo geral

GET /analytics/monthly – Vendas mensais

GET /analytics/top-products – Produtos mais vendidos

📥 Exemplo de Requisição

POST /sales

{
  "product_name": "Notebook",
  "quantity": 2,
  "unit_price": 3500.0,
  "sale_date": "2024-11-10"
}

▶️ Como Executar o Projeto
1️⃣ Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

2️⃣ Instalar dependências
python -m pip install -r requirements.txt

3️⃣ Subir a API
python -m uvicorn app.main:app --reload


Acesse:

http://127.0.0.1:8000/docs

📈 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

Consolidar conhecimentos em backend Python

Demonstrar lógica de negócio e análise de dados

Aplicar boas práticas de arquitetura

Servir como portfólio profissional