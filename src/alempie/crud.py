from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from .models import Account, Department
from sqlalchemy.exc import IntegrityError

# CRUD functies voor accounts en departments

async def get_all_accounts(db: AsyncSession):
    statement = select(Account).options(selectinload(Account.department))
    results = await db.execute(statement)
    return results.scalars().all()

async def get_all_departments(db: AsyncSession):
    statement = select(Department)
    results = await db.execute(statement)
    return results.scalars().all()

async def create_account(db: AsyncSession, name: str, description: str, department_id: int):
    try:
         new_account = Account(name=name, description=description, department_id=department_id)
         db.add(new_account)
         await db.commit()
         await db.refresh(new_account)
         return new_account
    except IntegrityError:
            await db.rollback() # Maak de foutieve actie ongedaan
            raise ValueError("Afdeling bestaat niet of data is incompleet.")