import psycopg2
from sqlalchemy import create_engine

def save_to_db(df):

    engine = create_engine(
        "postgresql://postgres:080502@localhost:5432/price_pipeline"
    )

    df.to_sql(
        "products",
        engine,
        if_exists="replace",
        index=False
    )

    print("✅ Dados salvos no PostgreSQL com sucesso!")