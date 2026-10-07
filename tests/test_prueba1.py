"""
Prueba #1: 
La siguiente prueba conlleva acabo el testing de un pedido
que ha sido enviado al cliente(Cocina), sin ser modificado 
antes.
El test debe fallar, sin romper el patrón.

Para correr esta prueba, ubicarse en SoftwareDesign y correr 
el siguiente comando: python -m pytest
"""
import pytest

from heladeria_Rumoroso.origenDePedidos import origenDePedido
from heladeria_Rumoroso.pedido import Pedido
from heladeria_Rumoroso.cocina import Cocina

def testPedido_SinModificar():
    class origenDeLaTienda(origenDePedido):
        def sigPedido(self):
            return Pedido(99,("menta",),"mediano","azucarado")
    pedido=Cocina(origenDeLaTienda()).prepararSig()
    assert pedido == Pedido(99,("menta",),"mediano","azucarado")