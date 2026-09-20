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

## operaciones inserciones busqueda modificacions y eliminacion 

## insercion 
# final de un arreglo  metodo append()

productos =['teclado', 'mouse','monitor', 'laptop']
productos.append("celullar tactil")
print(productos)

# insertar en una posison espesifica  insert

productos.insert(1 , "iphone")
print(productos)

# insertar varios elementos extend()
productos.extend(['hp', 'tv', 'asus', 'refrigerador' , 'tv'])
print(productos)


# ---busqueda ----
if 'tv' in productos:
    posicion = productos.index('tv')
    print (f'encontrado en la posision : {posicion}')
else :
    print(f'el elemento no se encontro')

print(productos.index('tv'))
print(productos.count('tv'))


# ------modificacion de elemento -----
productos[7]='licuadora'
print(productos)

for k in range(len(productos)):
    if productos[k]=='refrigeradora':
     productos[k]='airiculares'

print(productos)

# remplaza por cero a menor que 11 

print(notas)

for i in range(len(notas)):
    if notas[i]< 11:
        notas[i]= 0
print (notas)

#sumar +1 a cada notra 

for i in range(len(notas)):
    notas[i]=notas[i]+1
print (notas)

## modificacion por segmentos en mayusculas  con upper 
productos[1:3]=[producto.upper()for producto in productos[1:3]]
print(productos)


# modificacion por lista 
precio =[35,80,74,99]
precio =[precio*0.9 if precio  > 70 else precio for precio in precio]
print (precio)

# ----eliminacion ---
#eliminar un valor 
productos.remove('licuadora')
print(productos)

#eliminar por  indice metodo pop 

eliminado =productos.pop(2)
print("--------------------------")
print(eliminado)
print("--------------------------")
print(productos)

## eliminar por segmentos (rango difinido )

del productos[1:3]
print(productos)

## eliminar masiva  
notas = [x for x in notas if x < 12]
print (notas)

# vaciar lista 
notas.clear()
print(notas)