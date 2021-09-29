# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:11:53 2021

@author: ramon
"""

#IDENTIFICAR SE UMA SEQUENCIA DE NUCLEOTIDEOS PROMOVERA UMA PROTEINA FUNCIONAL OU DESFUNCIONAL

import pandas as pd
from sklearn.model_selection import train_test_split #Divide os dados em treino e teste
from sklearn.naive_bayes import GaussianNB #Utilizamos o Naive Bayes
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score #Utilizo matrizes de confusao
from yellowbrick.classifier import ConfusionMatrix

#################################################################################

genoma = pd.read_csv('gene.csv', sep=';') #Abro o dataset com os dados para aprendizado

print(genoma.shape)
print(genoma.head())

#################################################################################

categorias = genoma.iloc[:,0:3].values #Pego todas as linhas e colunas de 0 a 19 e transformo em matriz
classes = genoma.iloc[:,3] #Pego todas as linhas da coluna 20 e transformo em matriz

print(classes)

#################################################################################

#Para usar Naive Bayes, precisamos transformar colunas categoricas em numericas (com excecao da ultima coluna, que representa as classes)

labelencoder1 = LabelEncoder()
categorias[:,0] = labelencoder1.fit_transform(categorias[:,0])

labelencoder2 = LabelEncoder()
categorias[:,1] = labelencoder2.fit_transform(categorias[:,1])

labelencoder3 = LabelEncoder()
categorias[:,2] = labelencoder3.fit_transform(categorias[:,2])


#################################################################################

#Separamos os dados em 20% para teste e 80% para realizar o aprendizado

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(categorias, 
                                                                  classes, 
                                                                  test_size = 0.2,
                                                                  random_state = 0)

print(x_teste)
print(y_teste)

#################################################################################

#Realizamos a criacao do modelo de aprendizado propriamente dito (usando algoritmo Naive Bayes))
#Usamos os dados de treinamento

naive_bayes = GaussianNB()
naive_bayes.fit(x_treinamento, y_treinamento)

#################################################################################

#Agora vamos fazer a predicao dos dados de teste para o computador analisar se a proteina e funcional ou desfuncional
#Usamos os 20% dos dados, reservados para o teste

previsao = naive_bayes.predict(x_teste) #Usamos os dados das categorias do teste

print('Previsao: ', previsao)

#################################################################################

#Criamos a matriz de confusao para identificar os erros e acertos positivos e negativos

confusao = confusion_matrix(y_teste, previsao)
print('Matriz de Confusao: ', confusao)

#Taxa de acertos e erros

taxa_acerto = accuracy_score(y_teste, previsao)
taxa_erro = 1 - taxa_acerto

print('Taxa de Acerto: ', taxa_acerto)
print('Taxa de Erro: ', taxa_erro)

#Matriz de Confusao de forma Visual

v = ConfusionMatrix(GaussianNB())
v.fit(x_treinamento, y_treinamento)
v.score(x_teste, y_teste)
v.poof()


################################################################################

dadosnovos = pd.read_csv('novosgenes.csv', sep=';')

print('Cabecalho do CSV dos novos dados: ', dadosnovos.head())

categoriasnovas = dadosnovos.iloc[:,0:3].values

categoriasnovas[:,0] = labelencoder1.fit_transform(categoriasnovas[:,0])
categoriasnovas[:,1] = labelencoder2.fit_transform(categoriasnovas[:,1])
categoriasnovas[:,2] = labelencoder3.fit_transform(categoriasnovas[:,2])

resultado = naive_bayes.predict(categoriasnovas) 
print('Predicao dos novos dados: ', resultado)