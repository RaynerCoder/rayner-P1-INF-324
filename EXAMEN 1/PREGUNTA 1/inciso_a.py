"""
a. Con Python sin uso de librerías, calcule del ultimo cuartil, percentil 80 
por columna; explique qué significa en cada caso.
"""
import pandas as pd


#FUNCION 1: Calculo el percentil 80% y ultimo cuartil 75% de cada columna
def percentil(columna, porcentaje):
    k = porcentaje / 100
    columna = sorted(columna) #Ordenar la columna de menor a mayor
    n = len(columna)          #Longitud de la columna
    i = k*n                   #Calculamos la posicion del percentil
    
    #Verifico si i (posicion del percentil) es un numero entero o decimal
    if (i.is_integer()):
        #Entero
        i=int(i)
        pk = columna[i]
        
    else:
        #No entero, el percentil es el siguiente entero de la posicion i
        #Calculo la interpolacion linea para hallar el percentil, es �til 
        #cuando buscamos un valor entre puntos dados
        pos_ini = int(i)
        pos_fin = int(i) + 1
        valor_ini = columna[pos_ini]
        valor_fin = columna[pos_fin]
        pk = valor_ini + (i - pos_ini) * (valor_fin - valor_ini)

    return pk



#Datos - DataFrame
datos = pd.read_csv("obesidad.csv", sep=",")

for i in datos.columns:
    if i != "Sexo" and i != "CategoriaObesidad":
        print(i) #Nombre de la columna
        percentil_columna = percentil(datos[i], 80) #Calculo el percentil al 80%
        ultimoCuartil_columna = percentil(datos[i], 75) #Calculo el ultimo cuartil que seria el 75%
        
        print("Percentil      80% = ", percentil_columna)
        print("Ultimo Cuartil 75% = ", ultimoCuartil_columna)
        print("--------------------------------------------")