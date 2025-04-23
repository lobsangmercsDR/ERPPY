from app.modules.auth.models import User
from app.core.database import Base
from app.core.config import settings
import sys
import os
from logging.config import fileConfig
from typing import Any, Dict

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# 🧠 Agrega la carpeta raíz al path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

# 📦 Importa configuración y modelos


# Importa aquí todos tus modelos una vez existan
# from app.modules.users.models import User

# 🔧 Alembic Config object
config = context.config

# 🧪 Sobrescribe la URL de base de datos con la del entorno
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)  # type: ignore

# Logging (opcional)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Base metadata (lo que Alembic usará para detectar cambios)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecución en modo offline (genera SQL sin conexión)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecución en modo online (aplica directamente a la DB)."""
    config_section: Dict[str, Any] = config.get_section(
        config.config_ini_section) or {}

    connectable = engine_from_config(
        config_section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# 🚦 Lógica principal
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
