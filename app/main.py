from fastapi import FastAPI
from app.mems_router import router as router_memes


app = FastAPI()

app.include_router(router_memes)

