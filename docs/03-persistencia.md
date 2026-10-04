# Fase 06 - Persistencia de torneos

## Objetivo

Añadir persistencia para que los torneos no desaparezcan al cerrar o reconstruir la aplicación.

La aplicación permite actualmente:

- Crear un torneo.
- Sortear participantes.
- Guardar el torneo.
- Listar torneos guardados.
- Abrir un torneo.
- Borrar un torneo.

## Base de datos

Se utiliza SQLite.

Archivo:

data/tournaments.db

No se utiliza un servidor de base de datos independiente.

## Persistencia en Docker

En compose.yml se utiliza un volumen:

./data:/app/data

Esto conecta:

Servidor:

/home/luisde2001/stacks/tournament-maker/data

con:

Contenedor:

/app/data

De esta forma, tournaments.db permanece en el servidor aunque el contenedor se elimine o reconstruya.

## Archivo responsable

La lógica de acceso a SQLite está en:

app/database.py

## Tabla tournaments

La tabla principal se llama:

tournaments

Campos:

- id
- name
- participants
- draw
- created_at

## Formato de almacenamiento

La lista de participantes se almacena como JSON.

El cuadro del torneo también se almacena como JSON.

Esto permite recuperar exactamente el sorteo generado originalmente.

## Funciones principales

app/database.py contiene las funciones:

- init_db()
- save_tournament()
- list_tournaments()
- get_tournament()
- delete_tournament()

## Inicialización

La base de datos se inicializa automáticamente al arrancar Flask mediante:

init_db()

Si la tabla tournaments no existe, se crea automáticamente.

## Rutas web relacionadas

Listado de torneos:

/torneos

Abrir un torneo:

/torneos/<id>

Borrar un torneo:

/torneos/<id>/borrar

## Flujo de guardado

Usuario
↓
Introduce nombre y participantes
↓
Sortear y guardar
↓
Flask genera el cuadro
↓
SQLite guarda participantes y sorteo
↓
Se redirige al torneo guardado

## Comprobación manual de la base de datos

Desde la raíz del proyecto:

python - <<'PY'
import sqlite3

con = sqlite3.connect("data/tournaments.db")

rows = con.execute(
    "SELECT id, name, created_at FROM tournaments"
).fetchall()

print(rows)
PY

## Copias de seguridad

El archivo importante para conservar los torneos es:

data/tournaments.db

Al estar dentro de la carpeta del proyecto puede incluirse en el sistema habitual de copias del servidor.

No debe incluirse en GitHub si contiene datos reales de uso.

## Estado actual

SQLite funciona correctamente dentro del contenedor.

Los torneos permanecen después de:

- Reiniciar Docker.
- Ejecutar docker compose down.
- Reconstruir la imagen.
- Actualizar el código.

La persistencia depende del volumen:

./data:/app/data