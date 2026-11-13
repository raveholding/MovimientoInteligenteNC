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

**V26.70 (2026-11-12):** Atención al cliente → **🔌 Canales**: los 8 canales (tienda web y chat, WhatsApp Business, Instagram, Messenger, Telegram, correo, TikTok, Tiendanube) con «⚡ Conectar todo con un clic», asistente Rápido / Integrado y botones publicados para los socios. El modo integrado usa la función `canales` de Sistema VB (AlmacenRAVE/supabase/functions/canales) cuando el sistema trabaja con la nube.

`fuente/` es una copia de la fuente de Sistema VB (`AlmacenRAVE/fuente`, V26.65) con `p11-gym.js` y el perfil `nc`. Compilar: `cd fuente && python3 build.py nc ../index.html`.

Desarrollado por **Vincular Business** · Celular (387) 4484132 · https://www.vincularbusiness.com.ar/ · vincularbusiness@gmail.com · *“Tu idea, en buenas manos.”*

## Portero digital (`portero.html`)

Para la tablet o el celular de la entrada. Se abre desde Gimnasio › Acceso › "Abrir el portero".
- **Socios / alumnos:** entran con el QR dinámico de la app (lector USB o Bluetooth tipo teclado) o escribiendo su DNI. El portero lee los datos del sistema en el mismo equipo y valida la cuota: al día abre, en período de gracia abre con aviso, vencida, congelada o de baja no abre y ofrece llamar a Administración. Cada ingreso aparece solo en Control de acceso.
- Timbre por áreas con avisos al celular (ntfy o WhatsApp), timbre por QR desde el celular del visitante (`timbre.html`), pases de visita, PIN del equipo, PIN de coacción, tarjeta NFC, horarios, emergencia, asistente de voz y relé ESP32.
- Panel de configuración: doble toque en una zona libre de la pantalla. PIN de fábrica 1234 (cambiarlo en la puesta en marcha).
- Requisito: abrir el sistema al menos una vez en ese mismo equipo y navegador, para que el portero tenga los socios. La carpeta `face/` sólo se usa si se activa el reconocimiento facial del personal (apagado de fábrica).
