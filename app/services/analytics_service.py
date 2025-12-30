import pandas as pd
from sqlalchemy.orm import Session
from app.models.sale import Sale

def get_sales_dataframe(db: Session) -> pd.DataFrame:
    sales = db.query(Sale).all()

    data = [
        {
            "product_name": s.product_name,
            "quantity": s.quantity,
            "unit_price": s.unit_price,
            "sale_date": s.sale_date
        }
        for s in sales
    ]

    df = pd.DataFrame(data)
    return df


def summary_metrics(db: Session):
    df = get_sales_dataframe(db)

    if df.empty:
        return {
            "total_revenue": 0,
            "average_ticket": 0,
            "total_sales": 0
        }

    df["total_price"] = df["quantity"] * df["unit_price"]

    return {
        "total_revenue": float(df["total_price"].sum()),
        "average_ticket": float(df["total_price"].mean()),
        "total_sales": int(len(df))
    }


def monthly_sales(db: Session):
    df = get_sales_dataframe(db)

    if df.empty:
        return []

    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["month"] = df["sale_date"].dt.to_period("M")

    df["total_price"] = df["quantity"] * df["unit_price"]

    result = (
        df.groupby("month")["total_price"]
        .sum()
        .reset_index()
        .astype({"month": str})
        .to_dict(orient="records")
    )

    return result


def top_products(db: Session, limit: int = 5):
    df = get_sales_dataframe(db)

    if df.empty:
        return []

    df["total_price"] = df["quantity"] * df["unit_price"]

    result = (
        df.groupby("product_name")["total_price"]
        .sum()
        .sort_values(ascending=False)
        .head(limit)
        .reset_index()
        .to_dict(orient="records")
    )

    return result
