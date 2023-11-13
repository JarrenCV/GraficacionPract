# -*- coding: utf-8 -*-
"""Laboratorio #4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lgl6syQ-YU60ishVYj9qL0lXOXCrkGB6
"""

#Laboratorio #4
#Santiago Azofeifa Benavides
#Oscar Gutierrez Rosales
#Jarren Chaves Vizcaino
#Grupo 07

import pandas as pd

students = [('Ana', 23, 'San Jose', 'A'),
            ('Esteban', 22, 'Heredia', 'B'),
            ('Juan', 22, 'Cartago', 'A'),
            ('Karla', 22, 'Limon', 'A'),
            ('Ernesto', 21, 'Heredia', 'B'),
]
df= pd.DataFrame(students, columns =['Nombre', 'Edad', 'Ciudad', 'Seccion']) # Crea un Frame para la info
print(df)
def buscaPosicionYColumna(dfObj, value): #

  listOfPos = []  # Crea una lista de Posiciones
  result = dfObj.isin([value])  #Usa el metodo isin para buscar un objeto de value
  seriesObj = result.any()  # Crea una serie de bolleanos
  columnNames = list(seriesObj[seriesObj == True].index) # Crea una lista de columnas donde con lo nombres que encontró en index

  for col in columnNames:
    rows = list(result[col][result[col] == True].index)
# obtiene las columna donde se enonctró value

    for row in rows:
      listOfPos.append((row, col))
# agrega la poscicion linea/columna
  return listOfPos
# retorna la lita
listOfPositions = buscaPosicionYColumna(df,'A')

print('Index positions of 22 in Dataframe: ')

for i in range (len(listOfPositions)):
  print(listOfPositions[i])

dfp=pd.read_csv('/content/Shooting-and-Firearm-Discharges-Open-Data.csv')
data=pd.DataFrame(dfp)
print(data)

def buscaDato(dfObj, value): #

  listOfPos = []  # Crea una lista de Posiciones
  result = dfObj.isin([value])  #Usa el metodo isin para buscar un objeto de value
  seriesObj = result.any()  # Crea una serie de bolleanos
  columnNames = list(seriesObj[seriesObj == True].index) # Crea una lista de columnas donde con lo nombres que encontró en index

  for col in columnNames:
    rows = list(result[col][result[col] == True].index)
# obtiene las columna donde se enonctró value

    for row in rows:
      listOfPos.append((row, col))
# agrega la poscicion linea/columna
  return listOfPos




# retorna la lista
listaAnnio2006 = buscaDato(dfp,2006)

print('Sucesos que ocurrieron en el annio 2006: ')

for i in range (len(listaAnnio2006)):
  print(listaAnnio2006[i])

listaNoche = buscaDato(dfp,'Night')

print('Sucesos que ocurrieron en la noche: ')

for i in range (len(listaNoche)):
  print(listaNoche[i])
