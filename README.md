# Diseño de Software
## Patrón de Diseño Adapter
### Integrantes del grupo
- Victoria Molina Martínez 
- Luis Andrés Arrieta Víquez

### Heladería Rumoroso

#### Descripción del proyecto

Este proyecto es una implementación mínima del patrón de diseño Adapter en Python, usando como ejemplo una heladería llamada "Heladería Rumoroso". La cocina de la heladería ya funciona con un modelo propio, Pedido (id, sabores, size y cono), y se quiere que acepte también órdenes de plataformas de entregas externas sin modificarla. Para eso, Cocina (el Client) solo conoce la interfaz origenDePedido (el Target) y llama a su método sigPedido(). Las plataformas clienteRapi y ClienteMandados (los Adaptees) devuelven cada una su propio formato, y los adaptadores adaptadorRapi y adaptadorMandados (los Adapters) traducen esos formatos al Pedido que la cocina entiende.

#### Cómo se ejecuta y qué demuestra

Para ver el patrón en acción, se ejecuta desde la carpeta raíz:

```bash
python demo.py
```

El demo prepara un pedido desde RapiEntrega y otro desde Mandados usando la misma Cocina, y solo cambia el adaptador que se le entrega. 

Para correr ambas pruebas, se hace desde la carpeta raíz con el comando:

```bash
python -m pytest
```

Donde se requiere tener pytest instalado, además, se puede correr una prueba en específico, al ejecutar uno de los siguientes comandos:

```bash
python -m pytest tests/test_prueba1.py -v
python -m pytest tests/test_prueba2.py -v
```

#### Qué demuestra cada prueba

##### Prueba 1 (test_prueba1.py): 

Verifica que la Cocina acepta un origen nuevo que nunca vio sin modificarse.

##### Prueba 2 (test_prueba2.py): 

Verifica que la Cocina funciona con un adaptador nuevo, que se define en esta misma prueba, y se lo pasa a la misma Cocina que se usa con los adaptadores reales. 

En el caso de que dentro de la Cocina hubiera un `if` por tipo de adaptador, esta prueba fallaría, porque la Cocina rechazaría el adaptador nuevo.