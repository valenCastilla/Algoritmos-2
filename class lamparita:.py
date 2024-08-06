class lamparita: 

    def _init_(self,estado = False): 
        self.estado = estado


    def encender_lamparita(self): 
        self.estado = True
        return f'La lamparita esta prendida.'


    def apagar_lamparita(self): 
        self.estado = False
        return f'La lamparita esta apagada.'
    

    def estado_lamparita(self): 
        if self.estado == False: 
            estado = 'Apagado'
        else: 
            estado = 'Encendida'
        return f'El estado de la lamparita es: {estado}'
    

habitacionValen = lamparita(False) 

habitacionValen.encender_lamparita() 
habitacionValen.apagar_lamparita() 
habitacionValen.estado_lamparita() 
