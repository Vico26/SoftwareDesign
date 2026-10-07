# Prueba para ver que la Cocina funciona con cualquier adaptador
# Esta prueba comprueba que la Cocina no depende de un adaptador en específico

# En caso de que se agregara un if por tipo de adaptador dentro de la Cocina, la prueba fallaría

from ..cocina import Cocina
from ..origenDePedidos import origenDePedido
from ..pedido import Pedido

# Prueba de un adaptador nuevo, que se define en esta misma prueba
def test_cocina_funciona_con_adaptador_que_nunca_vio():
    
    class adaptadorMostrador(origenDePedido):
        def sigPedido(self) -> Pedido:
            return Pedido(
                id= 3,
                sabores = ("vainilla",),
                size = "mediano",
                cono = "sin cono"
            )
    
    # Se usa el mismo Cliente de Cocina que usamos con los adaptadores reales
    cocina = Cocina(adaptadorMostrador())

    # La cocina debe de aceptar el adaptador y devolver el Pedido ya traducido
    pedido = cocina.prepararSig()

    # Se debe verificar que el Pedido llegó como normalmente lo retornaría el adaptador
    assert isinstance(pedido, Pedido)
    assert pedido.sabores == ("vainilla",)
    assert pedido.size == "mediano"
    assert pedido.cono == "sin cono"