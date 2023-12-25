from beanie import PydanticObjectId
from fastapi import HTTPException, status

from src.models.task import Task


async def list_all_tasks():
    """Get a list off tasks"""
    tasks = await Task.find_all().to_list()
    return tasks


async def get_task_details(id: PydanticObjectId):
    """Get a task by id"""
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")

    return task


async def create_new_task(task: Task):
    """Create a task"""
    await task.insert()
    return task


async def update_a_task(id: PydanticObjectId, data):
    """Update a task"""
    task = await Task.get(id, data)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")
    _ = await task.update({"$set": data})
    updated_task = await Task.get(id)
    return updated_task


async def delete_a_task(id: PydanticObjectId):
    """Delete a task"""
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")
    await task.delete()
    return {"message": "Task deleted successfully"}
