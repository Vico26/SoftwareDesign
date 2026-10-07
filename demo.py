# Archivo para ejemplo de uso

from heladeria_Rumoroso.adaptadores import adaptadorMandados, adaptadorRapi
from heladeria_Rumoroso.adaptees import ClienteMandados, clienteRapi
from heladeria_Rumoroso.cocina import Cocina

def main() -> None:
    # El Pedido que llega desde RapiEntrega
    print("   Pedido desde RapiEntrega   ")
    cocinaRapi = Cocina(adaptadorRapi(clienteRapi()))
    cocinaRapi.prepararSig()

    # El Pedido que llega desde Mandados
    print("\n   Pedido desde Mandados   ")
    cocinaMandados = Cocina(adaptadorMandados(ClienteMandados()))
    cocinaMandados.prepararSig()

if __name__ == "__main__":
    main()