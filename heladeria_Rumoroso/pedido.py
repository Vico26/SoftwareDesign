#Se refiere a la clase de Pedido
from dataclasses import dataclass

@dataclass
class Pedido: #Es lo que Cocina entiende, osea es el modelo propio de la heladeria.
    id: int
    sabores: tuple
    size: str
    cono: str