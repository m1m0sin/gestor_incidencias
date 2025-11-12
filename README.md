# Gestor de Incidencias - Skeleton Repo

Proyecto de ejemplo para el curso DevOps: Gestor de Incidencias.
Contiene un esqueleto mínimo con FastAPI, SQLAlchemy, Podman Containerfile,
configuración básica de CI (GitHub Actions), y pruebas iniciales.

## Contenido
- app/: código fuente de la API
- tests/: pruebas pytest
- Containerfile: definition para construir imagen con Podman
- podman-compose.yml: orquestación local (app + db)
- .github/workflows/ci.yml: workflow CI básico
- requirements.txt: dependencias Python
- .pre-commit-config.yaml: hooks recomendados

## Instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
