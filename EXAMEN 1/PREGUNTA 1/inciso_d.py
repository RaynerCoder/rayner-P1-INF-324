import pandas as pd
import matplotlib.pyplot as plt

#Datos - DataFrame
datos = pd.read_csv('obesidad.csv')

#Se grafica para cada columna
for i in datos.columns:
    plt.figure(figsize=(8, 6))
    plt.hist(datos[i], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia Relativa')
    plt.title(f'Frecuencia de valores en {i}')
    plt.grid(True)
    plt.tight_layout() #Ajustar diseño para evitar superposiciones
    plt.show()