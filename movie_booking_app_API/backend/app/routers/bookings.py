
from fastapi import (APIRouter, Depends, HTTPException)

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db
from app.crud.crud import (create_booking, get_bookings)
from app.schemas.schemas import (BookingCreate, BookingResponse)

router = APIRouter(prefix="/bookings", tags=["bookings"])  

@router.post("/", response_model=BookingResponse)
async def book_ticket(booking: BookingCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_booking = await create_booking(db, booking)
        return new_booking
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[BookingResponse])
async def fetch_bookings(db: AsyncSession = Depends(get_db)):
    bookings = await get_bookings(db)
    return bookings
