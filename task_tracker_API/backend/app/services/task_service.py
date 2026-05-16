from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate
from app.schemas.task_schema import TaskUpdate

async def create_Task(db: AsyncSession, task_data: TaskCreate):
    new_task = Task(**task_data.model_dump())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task
async def get_all_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()
async def get_task_by_id(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()
async def update_Task(db: AsyncSession, task_id: int, task_data: TaskUpdate):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if task:
        for key, value in task_data.model_dump(exclude_unset=True).items():
            setattr(task, key, value)
        await db.commit()
        await db.refresh(task)
    return task
async def delete_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if task:
        await db.delete(task)
        await db.commit()
    return task