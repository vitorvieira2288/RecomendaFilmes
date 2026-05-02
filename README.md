Recomendador de Filmes com Streamlit


* Este projeto implementa um sistema de recomendação de filmes a partir das avaliações de usuários do dataset MovieLens.
* Dado um filme escolhido, o sistema sugere outros filmes semelhantes com base no comportamento coletivo dos usuários.


* Os dados de avaliações (ratings.csv) são combinados com os filmes (movies.csv).
* É criada uma matriz usuário × filme.
* Valores ausentes são preenchidos com 0.
* Calcula-se a similaridade entre filmes usando cosseno.
* O sistema recomenda os filmes mais similares ao selecionado.

Como executar
1. Clone o repositório
git clone https://github.com/vitorvieira2288/RecomendaFilmes.git

2. Instale as dependências
pip install pandas numpy scikit-learn streamlit
3. Execute o app
python -m streamlit run src/app.py  



O desempenho pode variar dependendo do tamanho do dataset.
Para grandes volumes de dados, recomenda-se otimizações adicionais.

Melhorias futuras possíveis:
* Verificação mais profunda de bugs eventuais
* Adicionar capas dos filmes 
* Implementar busca por nome 
* Deploy em nuvem 
* Filtragem por gênero
* Sistema híbrido 
