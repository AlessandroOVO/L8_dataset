import pandas as pd

#Leer el archivo y almacenarlo en un dataframe
df = pd.read_csv('bezdekIris.data', header = None) #header = None indica que el archivo no contiene una fila de encabezados. pd.read_csv devuelve un dataframe

print(df)