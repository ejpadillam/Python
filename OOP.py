class rectangulo:

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def __str__(self) -> str:
        return f"El rectangulo tiene de longitud: {self.longitud} y de ancho {self.ancho}"