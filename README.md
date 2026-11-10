# Movimiento Inteligente · Nahuel Cornu

Demo de un sistema de gestión para gimnasios y entrenadores personales. Son dos páginas: `index.html` (el sistema) y `menu.html` (menú público para nuevos socios),
que se abren directo en el navegador, sin instalar nada. Los datos quedan en el navegador (localStorage).

## Qué incluye

- **Dos modos:** entrenador personal (planes de 1, 2 y 3 sesiones semanales, presencial y virtual) y gimnasio completo.
- **Acceso:** validación por QR, NFC, huella o documento, con resultado verde, amarillo o rojo, bitácora y modo tótem.
- **Socios y cuotas:** estados al día, por vencer y vencidos, alertas, deuda de buffet y declaración de salud.
- **Club y WhatsApp:** sellos y premios, tarjeta con QR, cola de mensajes (vencimientos, cumpleaños, reactivación) y pedido de reseña.
- **Agenda y clases:** cupos, reservas y asistencia; sesiones personalizadas y programas de entrenamiento.
- **Buffet:** punto de venta, stock, vencimientos, cuenta corriente.
- **Cobros y facturas:** pagos mixtos, comprobantes internos y libro de ventas para llevar a ARCA.
- **Personal:** fichaje con PIN o NFC (rechaza repetidos en menos de 60 s), turnos, horas y liquidación estimada.
- **Administración:** caja del día, gastos, resultado del mes e informes, con exportación a CSV.
- **Roles:** administrador, supervisor y recepción ven distintas secciones.

## Menú público para nuevos socios

`menu.html` es la página que ve quien todavía no es socio: presentación, planes, horarios con reserva por WhatsApp, pasos para empezar y formulario de alta.

1. La persona completa el formulario y se le arma un mensaje de WhatsApp con un código de alta.
2. En el sistema, Club > Solicitudes > **Importar solicitud**: pegás el mensaje y queda en la lista.
3. **Aprobar y cobrar** la crea como socio con estado "Pendiente de primer pago"; no entra hasta el primer pago.
4. Al aprobar se puede enviar su tarjeta del Club (enlace y QR) por WhatsApp.

En Ajustes se cargan el WhatsApp del negocio, la dirección, la presentación y los horarios. Desde Club se copia el enlace del menú o se muestra su QR. Para publicarlo con GitHub Pages, la dirección es `https://raveholding.github.io/MovimientoInteligenteNC/menu.html` y se configura en Ajustes.
Los datos de cada navegador son locales: no hay sincronización en vivo entre dispositivos sin un servidor.

## Importante

- Los comprobantes son internos y no tienen validez fiscal. La factura electrónica se emite en ARCA.
- Huella y NFC se simulan en la demo. En producción necesitan un lector conectado y un programa que lo conecte.
- Los datos, teléfonos y precios que trae son de demostración.

## Desarrollo

Sistema desarrollado por **Vincular Business**: digitalización, software de gestión y fidelización para comercios y servicios de Argentina.
WhatsApp (387) 4484132 · vincularbusiness@gmail.com
