
from fastapi import (APIRouter, Depends, HTTPException)

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db
from app.schemas.schemas import (MovieCreate, MovieResponse)
from app.crud.crud import (create_movie, get_movies, delete_movie)

router = APIRouter(prefix="/movies", tags=["movies"])


@router.post("/", response_model = MovieResponse)
async def add_movie(movie: MovieCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_movie = await create_movie(db, movie)
        return new_movie
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[MovieResponse])
async def fetch_movies(db: AsyncSession = Depends(get_db)):
    movies = await get_movies(db)
    return movies

@router.delete("/{movie_id}")
async def remove_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    movie = await delete_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}


