def transform_data(df):

    print("🔄 Transformando dados...")

    # Separar rating
    df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
    df['rating_count'] = df['rating'].apply(lambda x: x['count'])

    # Selecionar colunas
    df = df[[
        'id',
        'title',
        'price',
        'category',
        'rating_rate',
        'rating_count'
    ]]

    print("✅ Dados transformados com sucesso!")

    return df