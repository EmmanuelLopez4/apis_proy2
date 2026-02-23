from fastapi import FastAPI
from routes.biometrico import router

app = FastAPI()

app.include_router(router)