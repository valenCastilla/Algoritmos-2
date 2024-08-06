class lamparita: 

    def _init_(self,estado): 
        self.estado = False 


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
    
