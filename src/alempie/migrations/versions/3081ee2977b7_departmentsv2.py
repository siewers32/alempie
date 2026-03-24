"""departmentsv2

Revision ID: 3081ee2977b7
Revises: a470bb389c56
Create Date: 2026-03-24 19:35:25.074241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = '3081ee2977b7'
down_revision: Union[str, Sequence[str], None] = 'a470bb389c56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
