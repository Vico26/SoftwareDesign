## Este archive tiene los adaptees
class clienteRapi:
    def __init__(self,orden=None):
        self._orden= orden or {
            "items":[{"sku": "HEL-VAN-2","cantidad": 1},
                     {"sku": "HEL-FRE-3","cantidad": 1}],
            "nota":"Sin cono, por favor"
        }
    def traerPedido(self)->dict:
        return self._orden

class ClienteMandados:
    def __init__(self,pedido=None):
        self._pedido= pedido or {
                    "lineas":[{"sabor": "chocolate"},
                             {"sabor": "fresa"}],
                    "size":"grande",
                    "cono":"waffle"
        }
    def obtenerPedido(self)->dict:
        return self._pedido