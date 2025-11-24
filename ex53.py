import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#Exibe as 5 primeiras linhas
print(df.head())

#Exibe as 5 primeiras linhas
print(df.tail())

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#Exibe o numero de linhas e colunas
print(df.shape)

#Exibe o nome das colunas
print(df.columns)

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#Exibe o numero de linhas e colunas
print("Número de linhas e colunas: ", df.shape)

#Exibe o nome das colunas
print("Resultado: ",df.columns)

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#Detlahe das colunas
for coluna in df.columns:
    print("Coluna: ",coluna)