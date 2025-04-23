"""Crear tabla items para inventario

Revision ID: d5df5908edcb
Revises: d91a8240e088
Create Date: 2025-04-23 14:58:37.226185
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd5df5908edcb'
down_revision: Union[str, None] = 'd91a8240e088'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: crear tabla items"""
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), primary_key=True,
                  autoincrement=True, nullable=False),
        sa.Column('nombre', sa.String(length=100), nullable=False),
        sa.Column('tipo', sa.String(length=50), nullable=False),
        sa.Column('talla', sa.String(length=20), nullable=False),
        sa.Column('genero', sa.String(length=10), nullable=False),
        sa.Column('codigo', sa.String(length=30), nullable=False, unique=True),
        sa.Column('descripcion', sa.Text(), nullable=True),
        sa.Column('estatus_renta', sa.Boolean(), nullable=True),
        sa.Column('condicion', sa.String(length=30), nullable=False),
        sa.Column('garantia', sa.Integer(), nullable=False),
        sa.Column('precio_alquiler', sa.Numeric(10, 2), nullable=False),
        sa.Column('marca', sa.String(length=50), nullable=True),
        sa.Column('stock_total', sa.Integer(), nullable=False),
        sa.Column('stock_alquilado', sa.Integer(), nullable=False),
        sa.Column('temporada', sa.String(length=50), nullable=True),
    )
    op.create_index('ix_items_id', 'items', ['id'], unique=False)
    op.create_index('ix_items_codigo', 'items', ['codigo'], unique=True)


def downgrade() -> None:
    """Downgrade schema: eliminar tabla items"""
    op.drop_index('ix_items_codigo', table_name='items')
    op.drop_index('ix_items_id', table_name='items')
    op.drop_table('items')
