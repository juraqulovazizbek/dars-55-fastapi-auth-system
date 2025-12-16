from fastapi import FastAPI

from app.db import engine, Base
from app.models import user, authtoken
from app.routers import users, auth

app = FastAPI(title='Auth System Api')

app.include_router(users.router)
app.include_router(auth.router)

Base.metadata.create_all(engine)
