import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(
    page_title="Recomendador de Filmes",
    
    layout="wide"
)

st.title(" Recomendador de Filmes")
st.markdown("Sistema de recomendação utilizando dataset MovieLens ")


@st.cache_data
def carregar_dados():
    ratings = pd.read_csv("data/ratings.csv")
    movies = pd.read_csv("data/movies.csv")
    return ratings, movies

@st.cache_data
def limpar_titulos(movies):
    import re
    
    def corrigir_titulo(title):
        
        title = re.sub(r'\s*\([^0-9].*?\)', '', title)
        
        
        if ', The' in title:
            title = title.replace(', The', '') 
            
            if '(' in title:
                titulo, ano = title.split('(', 1)
                title = f"The {titulo.strip()} ({ano.strip()}"
            else:
                title = f"The {title.strip()}"
                
        elif ', A' in title:
            title = title.replace(', A', '')
            if '(' in title:
                titulo, ano = title.split('(', 1)
                title = f"A {titulo.strip()} ({ano.strip()}"
            else:
                title = f"A {title.strip()}"
        
        
        title = re.sub(r'\s+', ' ', title).strip()
        
        return title
    
    movies['title'] = movies['title'].apply(corrigir_titulo)
    return movies
def preparar_dados(ratings, movies):
    df = ratings.merge(movies, on="movieId")
    return df

@st.cache_data
def criar_matriz(df):
    return df.pivot_table(
        index="userId", 
        columns="title", 
        values="rating"
    )

@st.cache_data
def calcular_similaridade(matriz):
    matriz = matriz.fillna(0)
    return cosine_similarity(matriz.T)


ratings, movies = carregar_dados()
movies = limpar_titulos(movies)
df = preparar_dados(ratings, movies)
matriz = criar_matriz(df)
similaridade = calcular_similaridade(matriz)



st.sidebar.header("🔍 Buscar Filme")


filmes_disponiveis = sorted(matriz.columns.tolist())


filme_selecionado = st.sidebar.selectbox(
    "Escolha um filme que você gostou:",
    options=filmes_disponiveis,
    index=filmes_disponiveis.index("Toy Story (1995)") if "Toy Story (1995)" in filmes_disponiveis else 0
)

n_recomendacoes = st.sidebar.slider(
    "Número de recomendações", 
    min_value=5, 
    max_value=50, 
    value=10, 
    step=1
)


if st.sidebar.button("🎬 Recomendar Filmes", type="primary"):

    try:
        idx = np.where(matriz.columns == filme_selecionado)[0][0]
        scores = list(enumerate(similaridade[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        
        recomendacoes = [matriz.columns[i[0]] for i in scores[1:n_recomendacoes+1]]
        
        
        st.success(f"**Filmes recomendados para quem gosta de:** {filme_selecionado}")
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.write("### 🎬 Recomendações:")
            for i, filme in enumerate(recomendacoes, 1):
                st.write(f"**{i}.** {filme}")
        
        
            
    except Exception as e:
        st.error(f"Erro ao gerar recomendações: {e}")


st.caption("Recomendação baseada em filtragem colaborativa • Streamlit")