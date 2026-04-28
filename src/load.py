import sqlite3
import os

def save_to_db(df):

    os.makedirs('database', exist_ok=True)

    conn = sqlite3.connect('database/products.db')

    df.to_sql(
        'products',
        conn,
        if_exists='replace',
        index=False
    )

    conn.close()

    print("Dados salvos no banco com sucesso!")