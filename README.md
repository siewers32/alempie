# Alembic test

### Alembic research
* FastApi
* Pydantic
* Pydantic settings
* SQLModel
* UV
* Python 3.12
* Postgres (docker)
* Alembic

### Project setup
* Installeer alempie als package

```shell
pyproject.toml
src/alempie
└── __init__.py # refereren naar modules met `from alempie.config import settings`
```

### Installatie
* uv `uv init --python 3.12`
* FastApi (`uv add "fastapi[standard]"`)
* Pydantic en settings zijn geinstalleerd met FastApi
* `uv add sqlmodel` installeert sqlalchemy en sqlmodel
* `uv add jinja2` template-engine

### Postgres (docker)
* Gebruik maken van een `named volume` om database-files op te slaan
* Gebruik maken van een `bind volume` om initialisatiescript te starten.
    * `mkdir postgres_init`

### Run
* `uv run fastapi dev src/alempie/main.py`

### Alembic
* `uv add alembic`
* `uv add psycopg2-binary` connectie naar postgres
* run `alembic init migrations` # Maak een map migrations aan met env.py etc.
* `uv pip install -e .`
* Stel `SQLALCHEMY_DATABASE_URI` samen uit .env credentials.
    * config.py
    * stel url in alembic/env.py in op `SQLALCHEMY_DATABASE_URI`
* Pas aan in alembic.ini `script_location = src/alempie/migrations`
* Verplaats map alembic -> src/alembie/migrations
* Pas `script.py.mako` aan om gebruik te kunnen maken van sqlmodel
    * Voeg toe: `import sqlmodel`
* Creëer migrations: `alembic revision --autogenerate -m "initial"`
* Creëer tabellen: `alembic ugrade head`


### Models
* Alembic maakt migrations op basis van SQLModel
* Voeg `from sqlmodel import SQLModel, create_engine` toe aan migrations/env.py
* Voeg de modellen toe aan env.py: `from alempie.models import MyModel`
* Verander `target_model = None` naar `target_metadata = SQLModel.metadata`
* Maak de folder `src/alempie/models`
* Definieer de models
* Maak een bestand `scr/alempie/modles/__init_py` om de models te exporteren
```
# src/pyfastic/models/__init__.py
from .account import Account
```
* Pas opnieuw env.py aan om aan te geven dat we SQLModel willen gebruiken
* De database url komt uit pydantic.settings (in config.py)
* Pas de funtie `run_migrations_online()` aan

```python
   # Maak een configuratie aan die jouw URI gebruikt
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.SQLALCHEMY_DATABASE_URI
    
    # Maak de engine aan met de juiste URL
    connectable = create_engine(settings.SQLALCHEMY_DATABASE_URI)

```

