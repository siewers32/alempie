from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from alempie.models.account import Account


class DepartmentBase(SQLModel):
    name: str
    description: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    accounts: List["Account"] = Relationship(back_populates="department")