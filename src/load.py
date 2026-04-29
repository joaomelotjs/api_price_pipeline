import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from src.logger import logger

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def save_to_db(df):
    
    logger.info("Salvando dados no PostgreSQL...")

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    df.to_sql(
        "products",
        engine,
        if_exists="replace",
        index=False
    )

    logger.info("Dados salvos no PostgreSQL com sucesso!")