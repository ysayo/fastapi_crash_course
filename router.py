from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import STask_add, STask, STask_id
from repository import TaskRepository


router = APIRouter(
    prefix = "/tasks",
    tags = ["Tasks"],
)

@router.post("")
async def add_task(
        task: Annotated[STask_add, Depends()],
) -> STask_id :
    task_id =  await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {"data": tasks}