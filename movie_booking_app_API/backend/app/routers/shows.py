from fastapi import (APIRouter, Depends, HTTPException)

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db

from app.schemas.schemas import (ShowCreate, ShowResponse)
from app.crud.crud import (create_show, get_shows)

router = APIRouter(prefix="/shows", tags=["shows"])

@router.post("/", response_model=ShowResponse)
async def schedule_show(show: ShowCreate, db: AsyncSession = Depends(get_db )):
    try:
        new_show = await create_show(db, show)
        return new_show
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ShowResponse])
async def fetch_shows(db: AsyncSession = Depends(get_db)):
    shows = await get_shows(db)
    return shows
