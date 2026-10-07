#Este archive tiene la clase abstracta de origenDepedidos
from abc import ABC, abstractmethod
from .pedido import Pedido ##Calling la clase de pedido

class origenDePedido(ABC):
    #Target: interfaz que Cocina espera
    @abstractmethod
    def sigPedido(self) -> Pedido:
        """Devuelve el prox pedidotraducido al modelo de la heladeria"""