import numpy as np

def recomendar_filmes(filme, matriz, similaridade, n=5):
    if filme not in matriz.columns:
        return []
    
    idx = np.where(matriz.columns == filme)[0][0]
    scores = list(enumerate(similaridade[idx]))
    
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    return [matriz.columns[i[0]] for i in scores[1:n+1]]