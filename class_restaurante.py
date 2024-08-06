class restaurante: 

    contador_restaurantes = 0
    salario = 2000

    def __init__(self, nombre, ciudad, nro_empleados):
        self.nombre = nombre
        self.ciudad = ciudad
        self.nro_empleados = nro_empleados
        restaurante.contador_restaurantes+= 1

    @classmethod
    def obtener_numero_restaurantes(cls):
        return cls.contador_restaurantes
    
    def calcular_costo_operativo(self): 
        return self.nro_empleados * restaurante.salario 
    

guerrin = restaurante('Guerrin', 'CABA', 100)
delicias = restaurante('Las delicias', 'San Martin', 50)
    
print('Numero de sucursales:', restaurante.obtener_numero_restaurantes())
print(f'Costo operativo de {guerrin.nombre}: ${guerrin.calcular_costo_operativo()}')
print(f'Costo operativo de {delicias.nombre}: ${delicias.calcular_costo_operativo()}')
