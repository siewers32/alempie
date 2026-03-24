from sqlmodel import Field, SQLModel


class AccountBase(SQLModel):
    name: str
    description: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
