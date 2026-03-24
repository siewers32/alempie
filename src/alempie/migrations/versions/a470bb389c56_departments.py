"""departments

Revision ID: a470bb389c56
Revises: 6e75521b1526
Create Date: 2026-03-24 19:33:19.699616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = 'a470bb389c56'
down_revision: Union[str, Sequence[str], None] = '6e75521b1526'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
