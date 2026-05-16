
from pydantic import (BaseModel, EmailStr, Field)

from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        from_attributes = True
        
class MovieCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    genre: str
    duration: int = Field(gt=0)
    language: str
    
class MovieResponse(BaseModel):
    id: int
    title: str
    genre: str
    duration: int
    language: str
    
    class Config:
        from_attributes = True
        
class TheatreCreate(BaseModel):
    name: str
    location: str
    total_seats: int = Field(gt=0)
    
class TheatreResponse(BaseModel):
    id: int
    name: str
    location: str
    total_seats: int
    
    class Config:
        from_attributes = True
        
class ShowCreate(BaseModel):
    movie_id: int
    theatre_id: int
    show_time: str
    price: float = Field(gt=0)
    
class ShowResponse(BaseModel): 
    id: int
    movie_id: int
    theatre_id: int
    show_time: str
    price: float
    
    class Config:
        from_attributes = True
        
class SeatResponse(BaseModel):

    id: int

    show_id: int

    seat_number: str

    is_booked: bool

    class Config:
        from_attributes = True
        
class BookingCreate(BaseModel):

    user_id: int

    show_id: int

    seat_id: int


class BookingResponse(BaseModel):

    id: int
    user_id: int
    show_id: int
    seat_id: int

    class Config:
        from_attributes = True

    