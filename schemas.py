from pydantic import BaseModel
from typing import Annotated, Optional


class STask_add(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STask_add):
    id: int


class STask_id(BaseModel):
    ok: bool = True
    task_id: int