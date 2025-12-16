from fastapi import FastAPI

from app.db import engine, Base
from app.models import user, authtoken

app = FastAPI(title='Auth System Api')

Base.metadata.create_all(engine)
