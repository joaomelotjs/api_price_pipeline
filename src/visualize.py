import matplotlib.pyplot as plt
import os

def generate_charts(df):

    print("📊 Gerando gráficos...")

    os.makedirs('output/charts', exist_ok=True)

    # Top produtos por avaliação
    top_products = df.sort_values(
        by='rating_rate',
        ascending=False
    ).head(10)

    plt.figure(figsize=(10,5))

    plt.barh(
        top_products['title'],
        top_products['rating_rate']
    )

    plt.title('Top Rated Products')
    plt.xlabel('Avaliação')
    plt.ylabel('Produto')

    plt.tight_layout()

    plt.savefig(
        'output/charts/top_rated_products.png'
    )

    plt.close()

    # Popularidade por categoria
    category_popularity = df.groupby(
        'category'
    )['rating_count'].sum()

    plt.figure(figsize=(8,5))

    category_popularity.plot(kind='bar')

    plt.title('Category Popularity')
    plt.xlabel('Categoria')
    plt.ylabel('Quantidade de avaliações')

    plt.tight_layout()

    plt.savefig(
        'output/charts/category_popularity.png'
    )

    plt.close()

    print("✅ Gráficos gerados com sucesso!")