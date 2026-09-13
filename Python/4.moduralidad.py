# modulos --> funciones espesificas

##calcular productos

def leer_prdocuto():
    return input("ingresar un producto")

def leer_precio():
    return float(input("ingrese un precio: "))

def calcular_igv(precio):
    return precio*0.18

def resultado(nombre,precio,igv):
    total=precio+igv
    print(f'producto : {nombre}')
    print(f'precio : {precio}')
    print(f'igv : {igv}')
    print(f'total a pagar  : {total}')
    
nombre=leer_prdocuto()
precio=leer_precio()
igv=calcular_igv(precio)
resultado(nombre,precio,igv)