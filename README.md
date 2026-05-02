Recomendador de Filmes com Streamlit


Este projeto implementa um sistema de recomendação de filmes a partir das avaliações de usuários do dataset MovieLens.
Dado um filme escolhido, o sistema sugere outros filmes semelhantes com base no comportamento coletivo dos usuários.


Python
Pandas
Scikit-learn
Streamlit

Os dados de avaliações (ratings.csv) são combinados com os filmes (movies.csv)
É criada uma matriz usuário × filme
Valores ausentes são preenchidos com 0
Calcula-se a similaridade entre filmes usando cosseno
O sistema recomenda os filmes mais similares ao selecionado

Como executar
1. Clone o repositório
git clone https://github.com/vitorvieira2288/RecomendaFilmes.git
cd seu-repo
2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate  # Windows
3. Instale as dependências
pip install pandas numpy scikit-learn streamlit
4. Execute o app
streamlit run app.py



O desempenho pode variar dependendo do tamanho do dataset
Para grandes volumes de dados, recomenda-se otimizações adicionais

Melhorias futuras possíveis
Verificação mais profunda de bugs eventuais
Adicionar capas dos filmes 
Implementar busca por nome 
Deploy em nuvem 
Filtragem por gênero
Sistema híbrido 
