from sqlmodel import Session, create_engine
from typing import Generator
import os
from .config import settings

url = settings.SQLALCHEMY_DATABASE_URI

engine = create_engine(
    url, 
    echo=True, 
)

def get_db() -> Generator[Session, None, None]:
    """
    Dependency die een database sessie levert aan FastAPI routes.
    Zorgt ervoor dat de sessie na gebruik altijd wordt gesloten.
    """
    with Session(engine) as session:
        yield session