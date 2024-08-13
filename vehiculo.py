class Vehiculo: 
    
    def __init__(self, marca:str , modelo: str, precioBase:float):
        self.marca = marca
        self.modelo = modelo
        self.precioBase = precioBase


    def __str__(self) -> str:
        return f'Marca: {self.marca}, modelo: {self.modelo}, precio base: {self.precioBase}'
    

    
    def calcularCostoAlquiler(self, dias:int):
        costo = self.precioBase * dias
        return print(costo)
    

class Auto(Vehiculo): 

    def __init__(self, marca: str, modelo: str, precioBase: float):
        super().__init__(marca, modelo, precioBase)
    
    def calcularCostoAlquiler(self, dias: int):
        costo = super().calcularCostoAlquiler(dias)
        return print(costo * 1.2)






VehiculoValen = Vehiculo('Toyota', 'Etios',1000)
VehiculoValen.calcularCostoAlquiler(1)
VehiculoValen.calcularCostoAlquiler(10)
VehiculoValen.calcularCostoAlquiler(150)

AutoValen = Auto('Toyota', 'Etios',1000)
VehiculoValen.calcularCostoAlquiler(150)
