import requests
import pandas as pd
from src.logger import logger

def extract_data():

    logger.info("Conectando na API...")

    url = "https://fakestoreapi.com/products"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data)

    logger.info(f"{len(df)} produtos extraídos com sucesso!")

    return df