# restringir acsesos a campos y valores 
class ctaAhorro:
    def __init__(self,titular,saldoinicial):
        self.titular=titular # publico
        self._saldo=saldoinicial #restringido
    
    def depositar(self,monto):
        if (monto > 0):
            self._saldo +=monto  #new saldo restringido
        
    def mostrar_saldo(self):
        print(f'titular :{self.titular}')
        print(f'saldo: {self._saldo:.2f}') #restringido
        
cuenta = ctaAhorro ("Elvis ", 1500)  # declarar una funcion para la clase cuenta ahorros
cuenta.depositar(500)
cuenta.mostrar_saldo()

            