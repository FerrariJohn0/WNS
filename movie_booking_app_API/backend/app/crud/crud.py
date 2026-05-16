
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import (User, Movie, Theatre, Show, Seat, Booking)

async def create_user(db: AsyncSession, user_data):
    
    new_user = User(**user_data.model_dump())
    
    db.add(new_user)
    
    await db.commit()
    await db.refresh(new_user)
    
    return new_user

async def get_users(db:AsyncSession):
    result = await db.execute(select(User))
    
    return result.scalars().all()

async def create_movie(db:AsyncSession, movie_data):
    new_movie = Movie(**movie_data.model_dump())
    
    db.add(new_movie)
    
    await db.commit()
    await db.refresh(new_movie)
    
    return new_movie

async def get_movies(db:AsyncSession):
    result = await db.execute(select(Movie))
    
    return result.scalars().all()

async def delete_movie(db:AsyncSession, movie_id: int):
    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    
    movie = result.scalar_one_or_none()
    
    if movie:
        await db.delete(movie)
        await db.commit()
        return True
    
    return False
async def create_theatre(db:AsyncSession, theatre_data):
    theatre = Theatre(**theatre_data.model_dump())
    
    db.add(theatre)
    
    await db.commit()
    await db.refresh(theatre)
    
    return theatre

async def get_theatres(db:AsyncSession):
    result = await db.execute(select(Theatre))
    
    return result.scalars().all()

async def generate_seats_for_show(db:AsyncSession, show_id:int):
    seat_rows = ["A", "B", "C", "D", "E", "F"]
    
    seats = []
    
    for row in seat_rows:
        for number in range(1, 11):
            seat = Seat(show_id=show_id, seat_number=f"{row}{number}", is_booked=False)
            seats.append(seat)
    db.add_all(seats)
    
    await db.commit()
    
    return seats

async def create_show(db:AsyncSession, show_data):
    show = Show(**show_data.model_dump())
    
    db.add(show)
    await db.commit()
    await db.refresh(show)
    
    await generate_seats_for_show(db, show.id)
    return show

async def generate_seats_for_show(db:AsyncSession, show_id:int):
    seat_rows = ["A", "B", "C", "D", "E", "F"]
    
    seats = []
    
    for row in seat_rows:
        for number in range(1, 11):
            seat = Seat(show_id=show_id, seat_number=f"{row}{number}", is_booked=False)
            seats.append(seat)
    db.add_all(seats)
    
    await db.commit()
    
    return seats
    

async def get_shows(db:AsyncSession):
    result = await db.execute(select(Show))
    
    return result.scalars().all()

async def get_available_seats(db:AsyncSession, show_id: int):
    result = await db.execute(select(Seat).where(Seat.show_id == show_id, Seat.is_booked == False))
    
    return result.scalars().all()
async def get_all_seats(
    db: AsyncSession,
    show_id: int
):

    result = await db.execute(
        select(Seat).where(
            Seat.show_id == show_id
        )
    )

    return result.scalars().all()
async def create_booking(db:AsyncSession, booking_data):
    result = await db.execute(select(Seat).where(Seat.id == booking_data.seat_id))
    
    seat = result.scalar_one_or_none()
    
    if not seat:
        raise Exception("Seat Not found")
    
    if seat.is_booked:
        raise Exception("Seat is already booked")
    
    seat.is_booked = True
    
    booking = Booking(**booking_data.model_dump())
    
    db.add(booking)
    
    await db.commit()
    await db.refresh(booking)
    
    return booking

async def get_bookings(db:AsyncSession):
    result = await db.execute(select(Booking))
    
    return result.scalars().all()


    

        

    


    