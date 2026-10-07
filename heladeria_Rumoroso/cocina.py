#Concina es el Client en este caso
from .pedido import Pedido
from .origenDePedidos import origenDePedido


class Cocina:
    def __init__(self, origen:origenDePedido):
        self._origen=origen
    def prepararSig(self)->Pedido:
        pedido=self._origen.sigPedido()
        print(f"Preparando:{', '.join(pedido.sabores)}|{pedido.size}|{pedido.cono}")
        return pedido
