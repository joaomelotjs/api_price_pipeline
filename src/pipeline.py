from src.extract import extract_data
from src.transform import transform_data
from src.load import save_to_db
from src.visualize import generate_charts
from src.logger import logger

def run_pipeline():

    logger.info("Iniciando pipeline...")

    df = extract_data()

    df = transform_data(df)

    save_to_db(df)

    generate_charts(df)

    logger.info("Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()