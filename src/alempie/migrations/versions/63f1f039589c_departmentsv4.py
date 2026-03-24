"""departmentsv4

Revision ID: 63f1f039589c
Revises: ac61df887119
Create Date: 2026-03-24 19:45:56.907163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = '63f1f039589c'
down_revision: Union[str, Sequence[str], None] = 'ac61df887119'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
