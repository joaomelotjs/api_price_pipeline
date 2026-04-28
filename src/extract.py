import requests
import pandas as pd

def extract_data():

    print("🌐 Conectando na API...")

    url = "https://fakestoreapi.com/products"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data)

    print(f"✅ {len(df)} produtos extraídos com sucesso!")

    return df