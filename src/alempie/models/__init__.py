# src/alempie/models/__init__.py

# Exporteer SQLModel zodat je het overal centraal hebt
from sqlmodel import SQLModel

# Importeer al je modellen
from .account import Account
from .department import Department

# Optioneel: Maak een lijst van wat je exporteert (voor 'from models import *')
__all__ = ["SQLModel", "Account", "Department"]