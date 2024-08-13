
class Trayecto: 

    def __init__(self, est_origen:str, est_destino:str, distancia:float, cant_est:int ) -> None:
        self.est_origen = est_origen
        self.est_destino = est_destino
        self.distancia = distancia
        self.cant_est = cant_est

    def __str__(self) -> str:
        return f"Trayecto de {self.est_origen} a {self.est_destino}, distancia: {self.distancia} km, estaciones: {self.cant_est}"


class TipoViaje: 

    def __init__(self, tipo) -> None:
        tipos_validos = ["diesel", "electrico", "alta velocidad"]
        if tipo.lower() in tipos_validos: 
            self.tipo = tipo.lower() 
        else: 
            raise ValueError(f"Tipo de viaje inválido: {tipo}")
        
    def __str__(self):
        return f"Tipo de viaje: {self.tipo}"
    

class Viaje: 

    def __init__(self, trayecto: Trayecto, cant_vagones: int, max_pasajeros:int, tipo_viaje:TipoViaje) -> None:

        if not isinstance(trayecto, Trayecto): 
            raise ValueError("Los trayectos no coinciden")

        if not isinstance(tipo_viaje, TipoViaje): 
            raise ValueError("Los tipos de viaje no coinciden")
        
        self.trayecto = trayecto 
        self.cant_vagones = cant_vagones
        self.max_pasajeros = max_pasajeros
        self.tipo_viaje = tipo_viaje


    def __str__(self) -> str:
        return (f"Viaje:\n{self.trayecto}\nCantidad de vagones: {self.cant_vagones}, "
                f"Capacidad máxima: {self.max_pasajeros} pasajeros\n{self.tipo_viaje}")
    
    def tiempoDeDemora(self) -> float:

        tipo = self.tipo_viaje.tipo
        
        if tipo.lower() == "diesel": 
            duracion = ((self.trayecto.distancia * self.trayecto.cant_est)/2) + ((self.trayecto.cant_est + self.max_pasajeros)/10)
            print(f'El tiempo de demora será de {duracion} minutos.')
            return duracion
        
        elif tipo.lower() == "electrico":
            duracion = ((self.trayecto.distancia * self.trayecto.cant_est)/2)
            print(f'El tiempo de demora será de {duracion} minutos.')
            return duracion
        
        elif tipo.lower() == "alta velocidad": 
            duracion = (self.trayecto.distancia / 10)
            print(f'El tiempo de demora será de {duracion} minutos.')
            return  duracion
        
        else: 
            raise ValueError(f"Tipo de viaje inválido: {tipo}")


trayecto1 = Trayecto("Estación A", "Estación B", 200, 5)
tipo_viaje1 = TipoViaje("Alta Velocidad")
viaje1 = Viaje(trayecto1, 10, 800, tipo_viaje1)
viaje1.tiempoDeDemora()
