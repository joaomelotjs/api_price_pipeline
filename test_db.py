import psycopg2

conn = psycopg2.connect(
    dbname="price_pipeline",
    user="postgres",
    password="080502",
    host="localhost",
    port="5432"
)

print("✅ Conectado com sucesso!")

conn.close()