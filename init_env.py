import os
import subprocess
import sys

VENV_DIR = "venv"
REQ_FILE = "requirements.txt"

# Crear entorno virtual si no existe
if not os.path.exists(VENV_DIR):
    print("🔧 Creando entorno virtual...")
    subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])

# Activar entorno virtual (no necesario en VSCode, pero útil en CLI)
venv_python = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "python")

# Instalar dependencias
if os.path.exists(REQ_FILE):
    print(f"📦 Instalando dependencias desde {REQ_FILE}...")
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([venv_python, "-m", "pip", "install", "-r", REQ_FILE])
else:
    print(f"⚠️ No se encontró {REQ_FILE}, se omite instalación.")
