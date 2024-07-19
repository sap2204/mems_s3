from fastapi import APIRouter

from app.dao import BaseDAO
from app.schema import SAddMem


router = APIRouter(
    prefix="/memes",
    tags=["Мемы"]
)


@router.get("")
async def get_all_memes():
    """Function for getting list of memes"""
    return await BaseDAO.get_all()



@router.get("/{id}")
async def get_mem_by_id(id: int):
    """Function for getting mem by id"""
    return await BaseDAO.get_mem_by_id(id)


@router.post("")
async def add_new_mem(name: str, url: str):
    """"Function for add a new mem"""
    await BaseDAO.add_mem(name=name, url=url)


@router.put("/{id}")
async def update_mem(id: int):
    """Function for update mem"""
    pass


@router.delete("{id}")
async def delete_mem(id: int):
    """Function for delete mem"""
    await BaseDAO.delete_mem_by_id(id)