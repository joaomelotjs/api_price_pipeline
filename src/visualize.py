import matplotlib.pyplot as plt
import os

def generate_charts(df):

    os.makedirs('output/charts', exist_ok=True)

    # TOP produtos por avaliação
    top_products = df.sort_values(
        by='rating_rate',
        ascending=False
    ).head(10)

    plt.figure(figsize=(10,5))

    plt.barh(
        top_products['title'],
        top_products['rating_rate']
    )

    plt.title('Top Produtos por Avaliação')

    plt.tight_layout()

    plt.savefig(
        'output/charts/top_products_rating.png'
    )

    plt.close()

    # Categorias mais populares
    category_popularity = df.groupby(
        'category'
    )['rating_count'].sum()

    plt.figure(figsize=(8,5))

    category_popularity.plot(kind='bar')

    plt.title('Popularidade por Categoria')

    plt.tight_layout()

    plt.savefig(
        'output/charts/category_popularity.png'
    )

    plt.close()

    print("Gráficos gerados com sucesso!")