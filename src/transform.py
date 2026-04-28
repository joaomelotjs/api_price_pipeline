def transform_data(df):

    # Separar rating em colunas
    df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
    df['rating_count'] = df['rating'].apply(lambda x: x['count'])

    # Selecionar colunas importantes
    df = df[[
        'id',
        'title',
        'price',
        'category',
        'rating_rate',
        'rating_count'
    ]]

    print("Dados transformados com sucesso!")

    return df