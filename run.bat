@echo off
setlocal

echo 🔁 Cargando variables de entorno desde .env...

REM Cargar el archivo .env
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

echo 📦 Ejecutando migraciones Alembic...
alembic upgrade head

echo 🚀 Iniciando servidor FastAPI en http://localhost:8000 ...
uvicorn app.main:app --reload

endlocal
pause
