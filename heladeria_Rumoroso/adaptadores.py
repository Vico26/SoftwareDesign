# Este archive contiene los adaptadores necesarios
from .origenDePedidos import origenDePedido
from .pedido import Pedido

CODIGOS_SABOR={"VAN":"vainilla","FRE":"fresa","CHO":"chocolate"}

class adaptadorRapi(origenDePedido):
    #Adapter: Traductor de formato de RapiEntrega al pedido de la heladeria.
    def __init__(self,client):
        self._client=client #Este representa al Adaptee

    def sigPedido(self) -> Pedido:
        orden=self._client.traerPedido()
        if not orden.get("items"):
            raise ValueError("La orden esta vacia")
        sabores=[]