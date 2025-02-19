from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.controllers.task_controller import TaskController
from api.schemas.task_schema import TaskCreate, TaskUpdate, TaskDelete
from api.utils.database import AsyncSessionLocal

router = APIRouter()
task_controller = TaskController()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/create", response_model=TaskCreate)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_controller.create_task(task, db)

@router.put("/update/{task_id}", response_model=TaskUpdate)
async def update_task(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    return await task_controller.update_task(task_id, task, db)

@router.delete("/delete/{task_id}", response_model=TaskDelete)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await task_controller.delete_task(task_id, db)
