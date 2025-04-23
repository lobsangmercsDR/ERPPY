@echo off
setlocal
echo 🛠️  Preparando entorno para FastAPI + Alembic

REM 1. Crear entorno virtual si no existe
if not exist .venv (
    echo 📦 Creando entorno virtual...
    python -m venv .venv
)

REM 2. Activar entorno virtual
call .venv\Scripts\activate

REM 3. Instalar dependencias
echo 📥 Instalando dependencias...
pip install -r requirements.txt

REM 4. Cargar variables de entorno desde .env
echo 🔐 Cargando variables de entorno desde .env...
for /f "usebackq delims=" %%A in (".env") do (
    set "line=%%A"
    if not "%%A"=="" (
        for /f "tokens=1,2 delims==" %%B in ("%%A") do (
            if not "%%B"=="" (
                set "%%B=%%C"
            )
        )
    )
)

REM 5. Ejecutar migraciones
echo 🔄 Aplicando migraciones Alembic...
alembic upgrade head

REM 6. Ejecutar servidor
echo 🚀 Iniciando FastAPI en http://localhost:8000 ...
uvicorn app.main:app --reload

endlocal
pause
