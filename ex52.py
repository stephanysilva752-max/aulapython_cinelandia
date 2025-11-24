import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

print(df.to_string())

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Artist']
print(filtro)

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Track']
print(filtro)

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Year']
print(filtro)

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Album']
print(filtro)