from alembic.environment import Optional
from sqlmodel import Field, Relationship, SQLModel


class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    # Gebruik een string "Department" in plaats van de klasse zelf
    department_id: int | None = Field(default=None, foreign_key="department.id")
    department: Optional["Department"] = Relationship(back_populates="accounts")