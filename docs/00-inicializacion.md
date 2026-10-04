# Fase 00 - Inicialización

## Objetivo

Crear la estructura base de Tournament Maker y dejar preparado el proyecto para su desarrollo, versionado con Git y futuro despliegue mediante Docker.

## Estructura inicial

```text
tournament-maker/
├── app/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   ├── tournament/
│   │   ├── __init__.py
│   │   └── knockout.py
│   ├── __init__.py
│   └── main.py
├── docs/
│   ├── 00-inicializacion.md
│   └── 01-eliminatorio-simple.md
├── tests/
│   ├── __init__.py
│   └── test_knockout.py
├── .gitignore
├── compose.yml
├── Dockerfile
├── README.md
└── requirements.txt

Tecnologías previstas
- Python
- Flask
- HTML
- CSS
- JavaScript
- Docker
- Git
- GitHub
Criterio de desarrollo
El proyecto se desarrollará por fases pequeñas y funcionales.
Cada fase deberá:
1. Añadir una funcionalidad concreta.
2. Incluir pruebas cuando sea necesario.
3. Mantener separada la lógica del torneo de la interfaz web.
4. Realizar un commit identificable antes de continuar.
Próxima fase
Fase 01: motor de torneo por eliminación directa.
