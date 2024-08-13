
class Publicacion: 

    def __init__(self, titulo:str, precio:float) -> None:
        self.titulo = titulo
        self.precio = precio 

    def __str__(self) -> str:
        return f"Publicación: {self.titulo}, Precio: ${self.precio}"


class Libro(Publicacion):

    def __init__(self, titulo: str, precio: float, total_paginas:int, año_publicacion:int) -> None:
        super().__init__(titulo, precio) 
        self.total_paginas = total_paginas
        self.año_publicacion = año_publicacion

    def __str__(self) -> str:
        return f"Libro: {self.titulo}, Páginas: {self.total_paginas}, Año: {self.año_publicacion}, Precio: ${self.precio} "


class Disco(Publicacion):
   
    def __init__(self, titulo: str, precio: float, cantidad_minutos:float) -> None:
        super().__init__(titulo, precio) 
        self.cantidad_minutos = cantidad_minutos

    def __str__(self) -> str:
        return f"Disco: {self.titulo}, Minutos: {self.cantidad_minutos}, Precio: ${self.precio} "
    

# Crear instancias de Libro y Disco
libro1 = Libro("El Quijote", 20.0, 500, 1605)
disco1 = Disco("The Dark Side of the Moon", 15.0, 42.0)

# Imprimir la información de las publicaciones
print(libro1)
print(disco1)

# Crear más instancias si lo deseas y probar otras combinaciones
# libro2 = Libro("Harry Potter y la Piedra Filosofal", 30.0, 400, 1997)