"""
c. Obtenga la media, mediana, moda y geométrica; explique la diferencia de los 
resultados y cuál de ellas se puede utilizar en un artículo científico
"""


import numpy as np
import pandas as pd
import statistics as stat
import math




def mediaGeometrica(columna):
    sumaLog = 0

    for dato in columna:
        sumaLog = sumaLog + math.log(dato)
    
    # Calcular la media geom�trica usando el logaritmo
    mediaLog = sumaLog / len(columna)
    
    # Calcular la media geom�trica original a partir del logaritmo
    media = math.exp(mediaLog)
    return media



#Datos - DataFrame
datos = pd.read_csv("obesidad.csv", sep=",")


for i in datos.columns:
    print(i)
    if i != "Sexo" and i != "CategoriaObesidad":
        print("->Media             = ", np.mean(datos[i]))
        print("->Mediana           = ", np.median(datos[i]))
        media_geometrica = mediaGeometrica(datos[i])
        print("->Media Geometrica  = ", media_geometrica)
        
    print("->Moda              = ", stat.mode(datos[i]))
    print("--------------------------------------------")



