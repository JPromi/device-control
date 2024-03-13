from fastapi import FastAPI
from controller import ping_router, power_router

app = FastAPI()

app.include_router(ping_router, prefix="/ping")
app.include_router(power_router, prefix="/system/power")