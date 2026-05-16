
from sqlalchemy import (Column, Integer, String, Float, Boolean, ForeignKey, UniqueConstraint)
from sqlalchemy.orm import relationship

from app.database.connection import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, nullable=False)
    
    email = Column(String, nullable=False, unique=True)
    
    bookings = relationship("Booking", back_populates="user")

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String, nullable=False)
    
    genre = Column(String, nullable=False)
    
    duration = Column(Integer)
    
    language = Column(String)
    
    shows = relationship("Show", back_populates="movie")
    
class Theatre(Base):
    __tablename__ = "theatres"
    
    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, nullable=False)
    
    location = Column(String, nullable=False)
    
    total_seats = Column(Integer, default=100)
    
    shows = relationship("Show", back_populates="theatre")
    
class Show(Base):
    __tablename__ = "shows"
    
    id = Column(Integer, primary_key=True, index=True)
    
    movie_id = Column(Integer, ForeignKey("movies.id"))
    
    theatre_id = Column(Integer, ForeignKey("theatres.id"))
    
    show_time = Column(String, nullable=False)
    
    price = Column(Float)
    
    movie = relationship("Movie", back_populates="shows")
    
    theatre = relationship("Theatre", back_populates="shows")
    
    bookings = relationship("Booking", back_populates="show")

    seats = relationship("Seat", back_populates="show")
    
class Seat(Base):
    __tablename__ = "seats"
    
    id = Column(Integer, primary_key=True, index=True)
    
    show_id = Column(Integer, ForeignKey("shows.id"))
    
    seat_number = Column(String, nullable=False)

    is_booked = Column(Boolean, default=False)
    
    show = relationship("Show", back_populates="seats")
    
    booking = relationship("Booking", back_populates="seat", uselist=False)
    
    __table_args__ = (UniqueConstraint("show_id", "seat_number", name="unique_show_seat"),)
    
class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True) 
    
    user_id = Column(Integer, ForeignKey("users.id"))
    
    show_id = Column(Integer, ForeignKey("shows.id"))
    
    seat_id = Column(Integer, ForeignKey("seats.id"))
    
    user = relationship("User", back_populates="bookings")
    
    show = relationship("Show", back_populates="bookings")
    
    seat = relationship("Seat", back_populates="booking")
    
    
    
    

    
    
