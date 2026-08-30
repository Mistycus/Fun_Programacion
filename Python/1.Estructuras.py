#Estructuras Secuencias 
print('Registro Basico')
nombre = input("Ingrese su Nombre: ")
edad = int(input("Ingrese su Edad: "))
print(f'Nombre: {nombre}')
print(f'Edad {edad}')

# Estructuras Condicionales
# Condicional Simple
print('validad edad : ')
if edad <18 :
    print('Eres Menor de Edad')

# Condicional Doble
if edad >17 :
    print('Eres Mayor de Edad')
else:
    print('Eres Menor de Edad.....')

# Condicional Multiple 
opcion =int(input('Ingrese un numero del 1 al 5: '))
match opcion:
    case 1: print('La primera opcion')
    case 2: print('La  segunda opcion')
    case 3: print('La tercera opcion')
    case _: print('Opcion no Validad')


# Condicional Anidado
if opcion==1:
    print('opcion 1')
elif opcion==2:
    print('opcion 2')
else:
    print ('opcion 3 ')


# Estructuras Repetitivas 
# For - Para
#Genera numeros del 1 al 5
for i in range(1, 6):
    print(f'Repeticion Numero: {i}')

# While - Mientras
contador = 1
while contador <=3:
    print(f"intento,{contador}")
    contador +=1  # Contador = Contar +1 

# Do While - Hacer Mientras
while True:
    numero = int (input('Ingrese un numero > 0 :'))
    if numero>0:
        break