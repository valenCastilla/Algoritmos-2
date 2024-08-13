class Punto: 

    def __init__(self, xs: float, ys:float) -> None:
        self.xs = xs 
        self.ys = ys
    
    def mostrar_punto(self): 
        print(f'Su punto es: ({self.xs} ; {self.ys})')

    def sumar_a_punto(self, x: float, y: float):
        self.xs = self.xs + x
        self.ys = self.ys + y

    def restar_a_punto(self, x: float, y: float):
        self.xs = self.xs - x
        self.ys = self.ys - y

    def multiplicar_punto(self, x: float, y: float):
        self.xs = self.xs * x
        self.ys = self.ys * y

    def sumar_puntos(self, PuntoB):
        self.xs = self.xs + PuntoB.xs
        self.ys = self.ys + PuntoB.ys
        print(f'El punto resultante es: ({self.xs} ; {self.ys})')

    
    def restar_puntos(self, PuntoB):
        self.xs = self.xs - PuntoB.xs
        self.ys = self.ys - PuntoB.ys
        print(f'El punto resultante es: ({self.xs} ; {self.ys})')

    
    def __eq__(self, otro: object) -> bool:
        return isinstance(otro, Punto) and (self.xs, self.ys) == (otro.xs, otro.ys)
            


PuntoA = Punto(1.88 , 3.33)
PuntoA.mostrar_punto()
PuntoC = PuntoA
#PuntoA.sumar_a_punto(1,1)
#PuntoA.mostrar_punto()
#PuntoA.restar_a_punto(5,5)
#PuntoA.mostrar_punto()
PuntoB = Punto(5,5)
PuntoA.sumar_puntos(PuntoB)
PuntoC.mostrar_punto()
print(PuntoA == PuntoC)