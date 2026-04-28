import requests
import pandas as pd

def extract_data():
    url = "https://fakestoreapi.com/products"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data)

    print("Dados extraídos com sucesso!")

    return df