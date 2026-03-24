from alembic.environment import Optional
from sqlmodel import Field, Relationship, SQLModel


class AccountBase(SQLModel):
    name: str
    description: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # Gebruik een string "Department" in plaats van de klasse zelf
    department_id: Optional[int] = Field(default=None, foreign_key="department.id")
    department: Optional["Department"] = Relationship(back_populates="accounts")
