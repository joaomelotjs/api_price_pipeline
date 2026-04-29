import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Conexão PostgreSQL
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Ler tabela do banco
df = pd.read_sql("SELECT * FROM products", engine)

# Título
st.title("📊 API Price Pipeline Dashboard")

st.caption("Dados carregados diretamente do PostgreSQL em tempo real")

# Consulta SQL
st.subheader("Consulta SQL")

st.code(
    "SELECT * FROM products;",
    language="sql"
)

# KPIs
st.subheader("Resumo Geral")

col1, col2, col3 = st.columns(3)

col1.metric("Total de Produtos", len(df))
col2.metric("Preço Médio", f"${df['price'].mean():.2f}")
col3.metric("Maior Avaliação", df['rating_rate'].max())

# Tabela
st.subheader("Tabela de Produtos")

st.dataframe(df)

# Gráfico por categoria
st.subheader("Produtos por Categoria")

category_count = df['category'].value_counts()

st.bar_chart(category_count)

# Top produtos
st.subheader("Top Produtos Avaliados")

top_products = df.sort_values(
    by='rating_rate',
    ascending=False
).head(10)

# Tabela
st.dataframe(
    top_products[
        ['title', 'price', 'rating_rate']
    ]
)

# Gráfico
st.bar_chart(
    top_products.set_index('title')['rating_rate']
)