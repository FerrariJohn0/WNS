
from fastapi import (APIRouter, Depends, HTTPException)

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db
from app.schemas.schemas import (UserCreate, UserResponse)
from app.crud.crud import (create_user, get_users)

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_user = await create_user(db, user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[UserResponse])
async def fetch_users(db: AsyncSession = Depends(get_db)):
    users = await get_users(db)
    return users


    
