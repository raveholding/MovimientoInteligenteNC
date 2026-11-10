# Movimiento Inteligente · Sistema de Nahuel Cornu

Sistema de gestión de **Movimiento Inteligente**, entrenamiento personalizado de Nahuel Cornu, sobre **Sistema Vincular Business** (base de un solo dueño, igual que raveV2) con el módulo **Entrenamiento**.

- Menú público con los planes: `/` · Acceso: `/#acceso`
- Usuarios iniciales: ADMIN 1234 · Supervisor 1111 · Mostrador 0000 · Entrenador 2468. **Cambiá los PIN** en Sistema › Usuarios y permisos.
- App del alumno: `/socio.html` (cada alumno recibe la suya por WhatsApp desde su ficha)

Trae **alumnos, cobros y rutinas de ejemplo** para verlo funcionando. Se borran desde Sistema › Configuración › Datos de la demo, y los planes y precios se ajustan en Entrenamiento › Planes.

## Módulo Entrenamiento

- **Alumnos:** ficha con estado del plan, progreso (mediciones y gráficos), programa e historial; congelar por vacaciones o lesión; avisos de vencimiento y riesgo de abandono por WhatsApp.
- **Agenda:** horarios fijos de cada alumno según su plan (1, 2 o 3 sesiones semanales), presencial o virtual, con asistencia.
- **Programas:** entrenador inteligente por reglas (objetivo, nivel, lesiones, equipamiento disponible y modalidad virtual en casa), con cargas editables, videos y envío por WhatsApp.
- **Planes:** 1, 2 o 3 sesiones semanales y programación virtual (precios de ejemplo). Se cobran en **Vender** (caja, comprobante y ARCA) y al cobrarse extienden el vencimiento.
- **Asistencia:** registro por QR de la app o documento.
- **Equipamiento:** estado y mantenimiento de los elementos.

Además: caja, inventario, Club de clientes, Atención al cliente, Recursos Humanos, facturación ARCA y menú público de Sistema VB.

## Límites

- Sin nube por ahora: los datos quedan en el navegador de este equipo. Hacé respaldos en Sistema › Importar / Exportar.
- El link de pago es fijo; el pago se confirma cobrando la cuota en Vender.
- WhatsApp asistido: cada mensaje lo envía una persona.

## Código

`fuente/` es una copia de la fuente de Sistema VB (`AlmacenRAVE/fuente`, V26.65) con `p11-gym.js` y el perfil `nc`. Compilar: `cd fuente && python3 build.py nc ../index.html`.

Desarrollado por **Vincular Business** · Celular (387) 4484132 · https://www.vincularbusiness.com.ar/ · vincularbusiness@gmail.com · *“Tu idea, en buenas manos.”*
