"""departmentsv3

Revision ID: ac61df887119
Revises: 3081ee2977b7
Create Date: 2026-03-24 19:38:39.626473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = 'ac61df887119'
down_revision: Union[str, Sequence[str], None] = '3081ee2977b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
