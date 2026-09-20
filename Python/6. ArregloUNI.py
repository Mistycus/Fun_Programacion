# declarando un arreglo

valores = [0,0,0,0]
print (valores) 

# irsertando valor en una posision 
valores[1]=25
# mostrando el arreglo
print (valores)
# tipo de dato arreglo

print (type(valores))

# logitud de un arreglo 
print (f'longitud es {len(valores)}')

#el ultimo elemento 
print(f'{valores[len(valores)-1]}')

# arreglo de nombres 
nombres = ['Elvis' ,' Raquel' ,' Juan' , 'Maycol', 'Edith']

print (f'cantidad de nombres guardados : {len(nombres)}')
print (f'ultimo nombre guardado : {nombres[len(nombres ) - 1]}')

edades =[23,14,18,25,17]
print (f'elemento en la posision 1 : {edades[1]}')
print (f'elemento en la posision 4 : {edades[4]}')

## recorrer un array arreglo lista vector 

notas = [12,16,18,10,12,11]
for i in range(len(notas)):
    print(f'posision {i} valor :{notas[i]}')

print(nombres)
for k in range(len(nombres)):
    print(f'Elemento {k+1}valor: {nombres[k]}')
