
from fastapi import FastAPI

from app.database.connection import (engine, Base)

from app.models.models import (User, Movie, Theatre, Show, Seat, Booking)

from app.routers import users
from app.routers import movies
from app.routers import theatres
from app.routers import shows
from app.routers import seats
from app.routers import bookings




app = FastAPI(title = "Movie Booking APP API", description="Backend API's for Movie Booking System")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
        
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(theatres.router)
app.include_router(shows.router)
app.include_router(seats.router)
app.include_router(bookings.router)


@app.get("/")
async def home():
    return "Movie Booking APP API running Successfully"