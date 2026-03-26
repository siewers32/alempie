from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class Department(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    accounts: List["Account"] = Relationship(back_populates="department")