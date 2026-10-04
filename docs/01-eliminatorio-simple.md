# Fase 01 - Eliminación directa

## Objetivo

Crear el motor que genere un torneo por eliminación directa a partir de una lista de participantes.

## Reglas

El cuadro principal debe tener un número de participantes igual a una potencia de 2:

- 2
- 4
- 8
- 16
- 32
- etc.

Si el número de participantes no coincide con una potencia de 2, se generará una ronda previa.

## Ejemplos

### 8 participantes

No hay ronda previa.

Cuadro principal:

8 participantes.

### 7 participantes

El cuadro principal será de 4.

Ronda previa:

- 3 partidos
- 6 participantes

Pase directo:

- 1 participante

Después de la ronda previa habrá:

- 3 ganadores
- 1 pase directo

Total:

4 participantes.

### 12 participantes

El cuadro principal será de 8.

Ronda previa:

- 4 partidos
- 8 participantes

Pase directo:

- 4 participantes

Después de la ronda previa habrá:

- 4 ganadores
- 4 pases directos

Total:

8 participantes.

## Comportamiento

El motor deberá:

1. Recibir una lista de participantes.
2. Mezclar aleatoriamente la lista.
3. Calcular el tamaño del cuadro principal.
4. Calcular cuántos participantes necesitan ronda previa.
5. Generar los emparejamientos de la ronda previa.
6. Identificar los participantes con pase directo.
7. Devolver una estructura de datos reutilizable por la web.

## Restricciones

- Mínimo 2 participantes.
- No se permitirán nombres vacíos.
- No se permitirán participantes duplicados.
- La lógica del torneo debe ser independiente de Flask y de la interfaz web.
