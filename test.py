from src.extract import extract_data
from src.transform import transform_data
from src.load import save_to_db
from src.visualize import generate_charts

df = extract_data()

df = transform_data(df)

save_to_db(df)

generate_charts(df)

print(df.head())