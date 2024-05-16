cont=0
def Generar_Combinaciones(lista, combinacion, k):
    if lista:
        Generar_Combinaciones(lista[1:], combinacion + [lista[0]], k)
        Generar_Combinaciones(lista[1:], combinacion, k)
    elif len(combinacion) == k:
        global cont
        cont=cont+1
        print(combinacion)


nodos = ['A', 'B', 'C', 'D' , 'E', 'F', 'G', 'H']  
combinacion = []
k = 2

print("\n========TODAS LAS POSIBLES COMBINACIONES========\n")
for i in range(len(nodos)):
    Generar_Combinaciones(nodos, combinacion, k)
    k=k+1
    

print("Total de combinaciones:", cont)