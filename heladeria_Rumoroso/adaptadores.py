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
        for i in orden["items"]:
            _,codigo,bolas=i["sku"].split("-") #Codigo de helado HEL-VAN-3
            if codigo not in CODIGOS_SABOR:
                raise ValueError(f"Codigo de sabor desconocido: {codigo}")
            sabores+=[CODIGOS_SABOR[codigo]]*int(bolas)*i["cantidad"]
        sinCono="sin cono" in orden.get("nota","").lower()
        #RapiEntregas no envia size, se asume grande
        return Pedido(tuple(sabores),"grande","sin cono" if sinCono else "waffle")
    