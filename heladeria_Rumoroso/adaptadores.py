# Este archivo contiene los adaptadores necesarios
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
        return Pedido(1, tuple(sabores),"grande","sin cono" if sinCono else "waffle")
    

class adaptadorMandados(origenDePedido):
    # Adapter para poder traducir el formato de Mandados al pedido de la heladería

    def __init__(self, client):
        # Un self._client para representar al Adaptee
        self._client = client
    
    def sigPedido(self) -> Pedido:
        orden = self._client.obtenerPedido()
        if not orden.get("lineas"):
            raise ValueError("La orden se encuentra vacía")
        
        # Se traduce cada linea de los Mandados a un sabor
        sabores = []
        for linea in orden["lineas"]:
            sabores.append(linea["sabor"])

        # Si el tamaño no está presente, se ocasiona un error, indicando que falta
        if "size" not in orden:
            raise ValueError("La orden de Mandados no trae el tamaño")
        size = orden["size"] 

        cono = orden.get("cono", "waffle")

        # Se retorna el Pedido traducido al formato que la cocina espera
        return Pedido(id = 2, sabores = tuple(sabores), size = size, cono = cono)