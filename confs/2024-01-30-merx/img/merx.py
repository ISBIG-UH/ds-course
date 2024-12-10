from typing import List

class Jugador:
    def __init__(self, ci: str, nombre: str, nivel: int, trofeos: int, trofeos_max: int):
        self.ci = ci
        self.nombre = nombre
        self.nivel = nivel
        self.trofeos = trofeos
        self.trofeos_max = trofeos_max

class Carta:
    def __init__(self, identificador: str, nombre: str, descripcion: str, costo: int, calidad: str):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.calidad = calidad

class Coleccionar:
    def __init__(self, jugador: Jugador, carta: Carta):
        self.jugador = jugador
        self.carta = carta

class MiBaseDeDatosComoClases:
    def __init__(self):
        self.conjunto_carta: List[Carta] = []
        self.conjunto_jugador: List[Jugador] = []
        self.conjunto_coleccionar: List[Coleccionar] = []

# Example usage:
# jugador = Jugador(ci='12345678', nombre='Juan', nivel=5, trofeos=10, trofeos_max=15)
# carta = Carta(identificador='001', nombre='Dragón de Fuego', descripcion='Un poderoso dragón.', costo=50, calidad='Alta')
# coleccionar = Coleccionar(jugador=jugador, carta=carta)
# base_datos = MiBaseDeDatosComoClases()
# base_datos.conjunto_carta.append(carta)
# base_datos.conjunto_jugador.append(jugador)
# base_datos.conjunto_coleccionar.append(coleccionar)
