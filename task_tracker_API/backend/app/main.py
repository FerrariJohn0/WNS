
from fastapi import FastAPI
from app.core.database import engine
from app.core.database import Base


from app.core.database import Base

from app.routes.task_routes import router as task_router

app = FastAPI( title= "Task Tracker API")

@app.get("/")
async def home():
    return { "message": "Task tracker API running"}

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(task_router)
