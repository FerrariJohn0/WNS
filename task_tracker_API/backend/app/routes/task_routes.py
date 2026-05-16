from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.schemas.task_schema import TaskCreate
from app.schemas.task_schema import TaskUpdate
from app.schemas.task_schema import TaskResponse

from app.services.task_service import create_Task
from app.services.task_service import get_all_tasks
from app.services.task_service import get_task_by_id
from app.services.task_service import update_Task
from app.services.task_service import delete_task as delete_task_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_Task(db, task)


@router.get("/", response_model=list[TaskResponse])
async def get_tasks(
    db: AsyncSession = Depends(get_db)
):
    return await get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    task = await get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: AsyncSession = Depends(get_db)
):
    task = await update_Task(
        db,
        task_id,
        task_data
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.delete("/{task_id}")
async def delete_task_route(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    task = await delete_task_service(
        db,
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }