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
    except Exception as e:
            await db.rollback() # Maak de foutieve actie ongedaan
            raise e

async def create_department(db: AsyncSession, name: str, description: str):
    try:
        new_department = Department(name=name, description=description)
        db.add(new_department)
        await db.commit()
        await db.refresh(new_department)
        return new_department
    except Exception as e:
        await db.rollback()
        raise e

async def update_account(
    db: AsyncSession, 
    account_id: int, 
    name: str, 
    description: str, 
    department_id: int
):
    try:
        # 1. Zoek het bestaande account
        statement = select(Account).where(Account.id == account_id)
        result = await db.execute(statement)
        db_account = result.scalar_one_or_none()

        if not db_account:
            return None # Of gooi een error als je dat liever hebt

        # 2. Pas de velden aan
        db_account.name = name
        db_account.description = description
        db_account.department_id = department_id

        # 3. Opslaan
        db.add(db_account)
        await db.commit()
        await db.refresh(db_account)
        return db_account

    except IntegrityError:
        await db.rollback()
        raise ValueError("Update mislukt: Afdeling bestaat niet of data is incompleet.")
    except Exception as e:
        await db.rollback()
        raise e

async def delete_account(db: AsyncSession, account_id: int):
    try:
        # 1. Zoek het account
        statement = select(Account).where(Account.id == account_id)
        result = await db.execute(statement)
        db_account = result.scalar_one_or_none()

        if db_account:
            # 2. Verwijder het object
            await db.delete(db_account)
            await db.commit()
            return True # Gelukt
        
        return False # Account bestond niet

    except Exception as e:
        await db.rollback()
        raise e