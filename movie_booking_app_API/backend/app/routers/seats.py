
from fastapi import (APIRouter, Depends)

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db
from app.crud.crud import (get_all_seats)
from app.schemas.schemas import (SeatResponse)

router = APIRouter(prefix="/seats", tags=["Seats"])

@router.get("/{show_id}", response_model=list[SeatResponse])
async def available_seats(show_id: int, db: AsyncSession = Depends(get_db)):
    seats = await get_all_seats(db, show_id)
    return seats

