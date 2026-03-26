from fastapi import FastAPI, Request, Depends
from httpx import request
from alempie.models.department import Department
from alempie.config import settings
from fastapi.responses import HTMLResponse
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

@app.get("/accounts", response_class=HTMLResponse)
async def list_accounts(request: Request, db: AsyncSession = Depends(get_db)):
    statement = select(Account).options(selectinload(Account.department))
    results = await db.execute(statement)
    accounts = results.scalars().all()

    return templates.TemplateResponse(
        request=request, 
        name="accounts/index.html", 
        context={"accounts": accounts}
    )

# @app.get("/departments", response_class=HTMLResponse)
# def list_departments(request: Request, db: Session = Depends(get_db)):
#     hello_text = "Hello World"
#     departments = db.exec(select(Department)).all()  # Haal alle departments op
    
#     return templates.TemplateResponse(
#         request=request, 
#         name="departments/index.html", 
#         context={"hello": hello_text, "departments": departments}
#     )

@app.get("/departments", response_class=HTMLResponse)
async def list_departments(request: Request, db: AsyncSession = Depends(get_db)):
    statement = select(Department)
    results = await db.execute(statement)
    
    # Gebruik .scalars().all() om een lijst van Department objecten te krijgen
    departments = results.scalars().all() 
    
    return templates.TemplateResponse(
        request=request,
        name="departments/index.html",
        context={"departments": departments}
    )

