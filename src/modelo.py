from sklearn.metrics.pairwise import cosine_similarity

def calcular_similaridade(matriz):
    matriz = matriz.fillna(0)
    return cosine_similarity(matriz.T)