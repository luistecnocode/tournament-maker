# Fase 02-05 - Web y despliegue

## Arquitectura

La aplicación utiliza:

- Python 3.12
- Flask
- Gunicorn
- Docker
- Nginx Proxy Manager
- GitHub

## Flujo de acceso

Internet
↓
https://torneos.luistecno.com
↓
Nginx Proxy Manager
↓
192.168.68.60:5010
↓
Docker
↓
Gunicorn :5000
↓
Flask

## Docker

Ruta del proyecto:

/home/luisde2001/stacks/tournament-maker

El contenedor se llama:

tournament-maker

## Puerto

El puerto publicado en compose.yml es:

5010:5000

Por tanto:

- Puerto del servidor: 5010
- Puerto interno del contenedor: 5000

## Gunicorn

Flask no se ejecuta con su servidor de desarrollo en producción.

Docker ejecuta:

gunicorn -b 0.0.0.0:5000 app.main:app

## Comandos habituales

Reconstruir:

docker compose down
docker compose up -d --build

Estado:

docker compose ps

Logs:

docker logs tournament-maker --tail 100

Ver todos los contenedores del servidor:

docker ps

## URL pública

https://torneos.luistecno.com

## DNS

torneos.luistecno.com
→ IP pública del servidor

## Nginx Proxy Manager

Proxy Host:

torneos.luistecno.com

Destino:

http://192.168.68.60:5010

## Estado actual

La aplicación está desplegada y accesible mediante HTTPS.

Nginx Proxy Manager recibe las conexiones externas y las reenvía al puerto 5010 del servidor.

Docker redirige ese puerto al puerto 5000 del contenedor.

Gunicorn sirve la aplicación Flask dentro del contenedor.