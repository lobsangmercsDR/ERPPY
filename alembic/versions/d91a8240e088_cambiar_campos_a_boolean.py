"""Cambiar campos a Boolean

Revision ID: d91a8240e088
Revises: 894b11b86811
Create Date: 2025-04-23 13:12:58.632445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd91a8240e088'
down_revision: Union[str, None] = '894b11b86811'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'users',
        'is_active',
        type_=sa.Boolean(),
        postgresql_using="is_active::boolean"
    )
    op.alter_column(
        'users',
        'is_superuser',
        type_=sa.Boolean(),
        postgresql_using="is_superuser::boolean"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'users',
        'is_superuser',
        type_=sa.INTEGER(),
        postgresql_using="is_superuser::int"
    )
    op.alter_column(
        'users',
        'is_active',
        type_=sa.INTEGER(),
        postgresql_using="is_active::int"
    )
