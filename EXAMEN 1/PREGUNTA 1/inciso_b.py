""".
b. Realice lo mismo del inciso (a) con el uso de numpy y pandas
"""

import numpy as np
import pandas as pd


#Datos - DataFrame
datos = pd.read_csv("obesidad.csv", sep=",")

for i in datos.columns:
    if i != "Sexo" and i != "CategoriaObesidad":
        print(i) #Nombre de la columna
        percentil_columna = np.percentile(datos[i], 80)#Calculo el percentil al 80%
        ultimoCuartil_columna = np.percentile(datos[i], 75)#Calculo el ultimo cuartil que seria el 75%
        
        print("Percentil      80% = ", percentil_columna)
        print("Ultimo Cuartil 75% = ", ultimoCuartil_columna)
        print("--------------------------------------------")
    
