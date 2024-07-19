from pydantic import BaseModel


class SAddMem(BaseModel):
    """Schema for add mem in DB for post-method"""
   # id: int
    name: str
    url: str