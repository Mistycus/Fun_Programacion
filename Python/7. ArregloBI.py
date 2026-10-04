## arreglos bidimencionales -matrices -tablas
## declarar una matriz
matriz = [
    [1,2,3] ,  # fila 1 
    [4,5,6] ,  # fila 2
]
print (matriz)
print (type(matriz))

matriz_2 =[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
print(matriz_2)
print (matriz_2[1][2])

# recorrer la matriz
print ('Recorrer la matriz')
for fila in range(len(matriz_2)):
    for columna in range(len(matriz_2[fila])):
        print(f'fila : {fila}, columna : {columna}, valor : {matriz_2[fila][columna]}' )

