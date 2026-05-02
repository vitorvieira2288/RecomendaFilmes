def preparar_dados(ratings, movies):
    df = ratings.merge(movies, on="movieId")
    return df

def criar_matriz(df):
    return df.pivot_table(
        index="userId",
        columns="title",
        values="rating"
    )