
from fastapi import (APIRouter, Depends, HTTPException)

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select

from app.schemas.schemas import (TheatreCreate, TheatreResponse)

from app.models.models import Theatre

from app.database.connection import get_db
from app.crud.crud import (create_theatre, get_theatres)

router = APIRouter(prefix="/theatres", tags=["theatres"])

@router.post("/", response_model=TheatreResponse)
async def add_theatre(theatre: TheatreCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_theatre = await create_theatre(db, theatre)
        return new_theatre
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[TheatreResponse])
async def fetch_theatres(db: AsyncSession = Depends(get_db)):
    theatres = await get_theatres(db)
    return theatres

@router.delete("/{theatre_id}")
async def remove_theatre(theatre_id: int, db: AsyncSession = Depends(get_db)):
    theatre = await db.execute(select(Theatre).where(Theatre.id == theatre_id))
    theatre = theatre.scalar_one_or_none()
    if not theatre:
        raise HTTPException(status_code=404, detail="Theatre not found")
    await db.delete(theatre)
    await db.commit()
    return {"message": "Theatre deleted successfully"}
