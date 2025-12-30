# 📊 Sales Analytics API

API REST desenvolvida em **Python com FastAPI** para **registro e análise de vendas**, aplicando boas práticas de arquitetura backend e processamento de dados.

O projeto permite cadastrar vendas, persistir dados em banco e gerar **métricas de negócio automaticamente**, simulando cenários reais de aplicações corporativas.

---

## 🚀 Funcionalidades

- Cadastro de vendas via API
- Persistência em banco de dados (**SQLite**)
- Análise de dados com **Pandas**
- Métricas de negócio:
  - Faturamento total
  - Ticket médio
  - Total de vendas
  - Vendas mensais
  - Produtos mais vendidos
- Documentação automática com **Swagger (OpenAPI)**

---

## 🛠️ Stack Tecnológica

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pandas
- SQLite
- Pydantic
- Uvicorn

---

## 🧱 Arquitetura do Projeto

```text
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
