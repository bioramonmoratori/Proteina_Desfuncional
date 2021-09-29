

#MACHINE LEARNING PARA IDENTIFICAR SE UMA PROTEINA SERÁ FUNCIONAL OU DESFUNCIONAL À PARTIR DE UMA SEQUENCIA DE NUCLEOTÍDEOS

Criamos um Protótipo para demonstrar a utilidade do Machine Learning para estudos preditivos na genética.
O exemplo apresentado não está relacionado com a realidade aplicável à genética, porém, é o primeiro passo para
começar a resolver problemas utilizando a bioinformática e análise de dados. 

O QUE UTILIZAREMOS PARA A PREDIÇÃO DAS SEQUÊNCIAS DE NUCLEOTÍDEOS?

- Arquivo 'gene.csv' contendo 20 exemplos de sequencias:
    - Arquivo destinado ao banco de dados para treino e teste;
    - Sêquencias separadas em 3 Códons;
    - A última coluna representa se a sequência dos 3 códons são funcionais ou desfuncionais;
    - As linhas são separadas entre 10 exemplos funcionais e 10 exemplos desfuncionais;
    - 80% desses dados serão usados para treinamento do modelo;
    - 20% desses dados serão usados para teste do modelo;
    
- Arquivo 'novosgenes.csv' contendo 3 novas sequencias aleatórias:
    - Arquivo destinado para as situações novas a serem aplicadas o modelo de aprendizado; 
    - A coluna final estará vazia pois ainda não sabemos se a proteína é funcional ou desfuncional;

- Código 'proteinadesfunciona.py':
    - Responsável por importar e manipular os arquivos .csv;
    - Cria, treina e testa o modelo utilizando-se do arquvio 'gene.csv' (80% dos dados para treino e 20% para teste)
    - Abre o arquivo 'novosgenes.csv' e usa o modelo criado anteriormente para fazer novas predições



     - github.com/bioramonmoratori