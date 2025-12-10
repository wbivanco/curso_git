# Taller Git + GitHub (Python)

Este repositorio se usa como plantilla para la demo del taller de Git y GitHub.

## Estructura del Proyecto

```
workshop_git/
├── app/
│   ├── __init__.py      # Hace que app sea un paquete Python
│   ├── main.py          # Aplicación principal
│   └── utils.py         # Funciones utilitarias (contiene greet)
├── tests/
│   └── test_app.py      # Tests con pytest
├── .github/
│   └── workflows/
│       └── ci.yml       # Workflow de CI con GitHub Actions
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Este archivo
└── INSTRUCCIONES.md     # Guía completa del ejercicio
```

## Características

- ✅ App simple en Python con función de saludo
- ✅ Tests automatizados con `pytest`
- ✅ Workflow de CI con GitHub Actions
- ✅ Guía paso a paso en `INSTRUCCIONES.md`

## CI/CD

El repositorio incluye un workflow de GitHub Actions (`.github/workflows/ci.yml`) que:

- Se ejecuta automáticamente en cada push a las ramas `main` y `develop`
- Se ejecuta en cada Pull Request hacia `main` o `develop`
- Prueba el código con Python 3.9, 3.10 y 3.11 (matriz de versiones)
- Instala dependencias desde `requirements.txt`
- Ejecuta todos los tests con `pytest`

Los resultados aparecen como "checks" en los Pull Requests. Todos los tests deben pasar para que el check esté verde ✅.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar Tests

```bash
python -m pytest tests/
```

## Ejecutar la Aplicación

```bash
python -m app.main
```
