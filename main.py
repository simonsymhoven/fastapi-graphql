from fastapi import FastAPI

from api.controllers.user import user

app = FastAPI(redoc_url=None, docs_url=None)
app.include_router(user)
