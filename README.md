# Diseño de Software
## Patrón de Diseño Adapter
### Integrantes del grupo
- Victoria Molina Martínez 
- Luis Andrés Arrieta Víquez

### Heladería Rumoroso

*Descripción del proyecto*
Este proyecto es una implementación mínima del patrón de diseño Adapter en Python, usando como ejemplo una heladería llamada "Heladería Rumoroso". La cocina de la heladería ya funciona con un modelo propio, Pedido (id, sabores, size y cono), y se quiere que acepte también órdenes de plataformas de entregas externas sin modificarla. Para eso, Cocina (el Client) solo conoce la interfaz origenDePedido (el Target) y llama a su método sigPedido(). Las plataformas clienteRapi y ClienteMandados (los Adaptees) devuelven cada una su propio formato, y los adaptadores adaptadorRapi y adaptadorMandados (los Adapters) traducen esos formatos al Pedido que la cocina entiende.

*Cómo se ejecuta y qué demuestra*

Para ver el patrón en acción, ejecuta python demo.py desde la carpeta raíz: la demo prepara un pedido desde RapiEntrega y otro desde Mandados usando la misma Cocina, y solo cambia el adaptador que se le entrega. Las pruebas se corren con python -m pytest *y requieren tener pytest instalado*. Hay dos pruebas que representan la idea central del patrón: la primera verifica que Cocina acepta un origen nuevo que nunca vio sin modificarse.