from fastapi import FastAPI, Request
from .config import settings
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title=settings.PROJECT_NAME)

templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")


@app.get("/")
def read_root(request: Request):
    hello_text = "Hello World"
    
    return templates.TemplateResponse(
        request=request,             # Expliciet benoemen!
        name="home/index.html",      # Expliciet benoemen!
        context={"hello": hello_text} # De rest van je variabelen
    )