# Fase 07-08 - Exportación PDF y acceso privado

## Exportación PDF

La aplicación permite descargar un PDF de cada torneo guardado.

La librería utilizada es:

ReportLab

La lógica de generación se encuentra en:

app/pdf_generator.py

## Formato del PDF

El PDF está pensado para impresión.

Características:

- Tamaño A4.
- Orientación horizontal.
- Márgenes reducidos.
- Distribución compacta.
- Nombre del torneo.
- Número de participantes.
- Nombre de cada ronda.
- Identificador de cada partido.
- Nombres de los participantes.
- Ronda previa cuando sea necesaria.
- Octavos, cuartos, semifinales y final según el tamaño del cuadro.

## Ruta de descarga

La ruta Flask utilizada es:

/torneos/<id>/pdf

Al abrir un torneo guardado aparece el botón:

Descargar PDF

La descarga se genera dinámicamente a partir de los datos almacenados en SQLite.

## Archivo responsable

Generación del PDF:

app/pdf_generator.py

Ruta HTTP y descarga:

app/main.py

## Dependencia

requirements.txt incluye:

reportlab==4.4.4

## Flujo de descarga

Usuario
↓
Abre un torneo guardado
↓
Pulsa Descargar PDF
↓
Flask recupera el torneo de SQLite
↓
ReportLab genera el PDF en memoria
↓
Flask envía el fichero al navegador

No es necesario guardar previamente el PDF en el servidor.

## Acceso privado

La aplicación está protegida desde Nginx Proxy Manager.

No se ha implementado un sistema propio de usuarios dentro de Flask.

La autenticación se produce antes de que la petición llegue a Tournament Maker.

## Access List

Nombre de la Access List:

Torneos privado

La lista se asigna al Proxy Host:

torneos.luistecno.com

## Usuario

El acceso utiliza autenticación HTTP Basic.

El nombre de usuario configurado es:

luisde2001

La contraseña no debe almacenarse en:

- GitHub.
- README.md.
- docs/.
- compose.yml.
- Código fuente.

## Configuración de acceso

La Access List utiliza una regla que permite cualquier dirección IP, pero exige autenticación.

Reglas:

allow 0.0.0.0/0
deny all

Satisfy Any:

Desactivado

Pass Auth to Host:

Desactivado

## Flujo completo de acceso

Internet
↓
https://torneos.luistecno.com
↓
Nginx Proxy Manager
↓
Autenticación usuario y contraseña
↓
Proxy hacia 192.168.68.60:5010
↓
Docker
↓
Gunicorn
↓
Flask
↓
Tournament Maker

## HTTPS

El certificado SSL se gestiona desde Nginx Proxy Manager mediante Let's Encrypt.

El acceso público se realiza mediante:

https://torneos.luistecno.com

## Seguridad actual

La aplicación no está abierta directamente al público.

Para acceder se necesita superar la autenticación configurada en Nginx Proxy Manager.

La base de datos SQLite no está expuesta a Internet.

El puerto interno de Flask es:

5000

El puerto publicado en el servidor es:

5010

El acceso normal debe hacerse mediante el dominio HTTPS y no directamente mediante el puerto.

## Estado actual

La aplicación está:

- Desplegada con Docker.
- Servida con Gunicorn.
- Protegida mediante Nginx Proxy Manager.
- Accesible mediante HTTPS.
- Protegida con usuario y contraseña.
- Preparada para generar PDFs imprimibles.