from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, status

from src.crud.task import (
    create_new_task,
    delete_a_task,
    get_task_details,
    list_all_tasks,
    update_a_task,
)
from src.models.task import Task

task_router = APIRouter()


@task_router.get("/", response_model=List[Task])
async def list_tasks():
    return await list_all_tasks()


@task_router.get("/{task_id}", response_model=Task)
async def retrive_task(task_id: PydanticObjectId):
    return await get_task_details(task_id)


@task_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Task)
async def create_task(task: Task):
    return await create_new_task(task)


@task_router.put("/{task_id}", response_model=Task)
async def update_task(task_id: PydanticObjectId, task_data: Task):
    return await update_a_task(task_id, task_data)


@task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: PydanticObjectId):
    return await delete_a_task(task_id)
