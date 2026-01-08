import requests
import ast #Ajuda a processar (trabalhar) com dados em formato de texto
import nltk #Ajuda a processar (trabalhar) com dados em formato de texto
import sklearn
import numpy as np
import pandas as pd
from nltk.stem.porter import PorterStemmer #função para realizar o pré-processamento dos dados textuais.
from sklearn.feature_extraction.text import CountVectorizer #função para vetorizar os dados. Ou seja, transforma os dados textuais em dados numéricos.
#isso se chama vetorizaçao.
from sklearn.metrics.pairwise import cosine_similarity #para calcular a similaridade (dada pela distância) entre os vetores.
pd.options.mode.chained_assignment = None

df_filmes = pd.read_csv('dados/dataset_filmes.csv')
df_elento = pd.read_csv('dados/dataset_elenco.csv')
filmes = df_filmes.merge(df_elento, on= 'title')
#print(filmes.shape)
#print(filmes.info())

df_final_filmes = filmes [['movie_id', 'title', 'genres', 'overview', 'keywords', 'cast', 'crew']]
#print(df_final_filmes.head())

#identifa e soma o número de valores ausentes em cada coluna
#print(df_final_filmes.isnull().sum())
#print("------------------------------------------------------")
#remover linhas com valores ausentes
#df_final_filmes.dropna(inplace=True)
#print(df_final_filmes.isnull().sum())

#Tem valores duplicados?
#print(df_final_filmes.duplicated().sum())

#processamento de textos com AST - abstract syntax tree. Vamos começar ajustando a coluna de gênero de filme. Nesta coluna, precisamos apenas dos nomes e não dos ids.
# Função de conversão
# Este loop itera sobre os elementos de uma estrutura de dados. 
# Usamos ast.literal_eval(obj) para avaliar/converter a string obj em uma estrutura de dados Python.
def converter(obj):
  L = []
  for i in ast.literal_eval(obj):
    L.append(i['name'])
  return L

# Aplica-se, então, a função ao nosso dataset, nas colunas genres e keywords do filme
df_final_filmes['genres'] = df_final_filmes['genres'].apply(converter)
df_final_filmes['keywords'] = df_final_filmes['keywords'].apply(converter)
print(df_final_filmes['keywords'].head())

