from fastapi import FastAPI
from api.controllers.index import user

app = FastAPI()
app.include_router(user)