from fastapi import FastAPI, Request, Depends, Form
from httpx import request
from alempie import crud
from alempie.models.department import Department
from alempie.config import settings
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlmodel import select
from alempie.models import *
from alempie.database import get_db

app = FastAPI(title=settings.PROJECT_NAME)

templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    hello_text = "Hello World"
    
    return templates.TemplateResponse(
        request=request, 
        name="home/index.html", 
        context={"hello": hello_text}
    )

# @app.get("/accounts", response_class=HTMLResponse)
# async def list_accounts(request: Request, db: AsyncSession = Depends(get_db)):
#     statement = select(Account).options(selectinload(Account.department))
#     results = await db.execute(statement)
#     accounts = results.scalars().all()
#     statement = select(Department)
#     results = await db.execute(statement)
#     departments = results.scalars().all()

#     return templates.TemplateResponse(
#         request=request, 
#         name="accounts/index.html", 
#         context={"accounts": accounts, "departments": departments}
#     )

# @app.get("/departments", response_class=HTMLResponse)
# async def list_departments(request: Request, db: AsyncSession = Depends(get_db)):
#     statement = select(Department)
#     results = await db.execute(statement)
    
#     # Gebruik .scalars().all() om een lijst van Department objecten te krijgen
#     departments = results.scalars().all() 
    
#     return templates.TemplateResponse(
#         request=request,
#         name="departments/index.html",
#         context={"departments": departments}
#     )

# @app.post("/accounts")
# async def create_account(request: Request, db: AsyncSession = Depends(get_db)):
#     params = await request.form()
#     name = params.get("name")
#     description = params.get("description")
#     department_id = params.get("department_id")
#     new_account = Account(
#         name=name,
#         description=description,
#         department_id=department_id
#     )
#     db.add(new_account)
#     await db.commit()
#     accounts = await list_accounts(request, db)
#     departments = await list_departments(request, db)
#     return templates.TemplateResponse(
#         request=request,
#         name="accounts/index.html",
#         context={"accounts": accounts, "departments": departments}
#     )

@app.get("/accounts", response_class=HTMLResponse)
async def list_accounts_page(request: Request, db: AsyncSession = Depends(get_db)):
    # Hergebruik de functies uit crud.py
    accounts = await crud.get_all_accounts(db)
    departments = await crud.get_all_departments(db)
    
    return templates.TemplateResponse(
        request=request,
        name="accounts/index.html",
        context={
            "accounts": accounts, 
            "departments": departments
        }
    )

@app.post("/accounts/add")
async def add_account(
    db: AsyncSession = Depends(get_db),
    name: str = Form(...),
    description: str = Form(...),
    department_id: int = Form(...)
):
    await crud.create_account(db, name=name, description=description, department_id=department_id)
    # Na toevoegen sturen we de gebruiker terug naar de lijst
    return RedirectResponse(url="/accounts", status_code=303)


@app.get("/departments", response_class=HTMLResponse)
async def list_departments_page(request: Request, db: AsyncSession = Depends(get_db)):
    # Hergebruik de functies uit crud.py
    departments = await crud.get_all_departments(db)
    
    return templates.TemplateResponse(
        request=request,
        name="departments/index.html",
        context={
            "departments": departments
        }
    )
