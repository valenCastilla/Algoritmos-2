class monedero: 

    def __init__(self, dinero):
        self.dinero = dinero 

    def agregar_dinero(self,dinero):
        self.dinero = self.dinero + dinero

    def quitar_dinero(self,dinero): 
        if dinero <= self.dinero: 
            self.dinero= self.dinero - dinero 
        else: 
            print('Saldo Insuficiente. Seleccione una cantidad menor para retirar.')

    def mostrar_dinero(self):
        print(self.dinero)


BilleteraValen = monedero(200)
BilleteraValen.mostrar_dinero()
BilleteraValen.agregar_dinero(100)
BilleteraValen.mostrar_dinero()
BilleteraValen.quitar_dinero(50)
BilleteraValen.mostrar_dinero()
BilleteraValen.quitar_dinero(300)