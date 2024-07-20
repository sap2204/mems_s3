from fastapi import APIRouter, UploadFile

from app.dao import BaseDAO
from app.s3_storage import s3_client



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


@router.post("/foto", status_code=201)
async def add_mem(upload_file: UploadFile):
    file =  await upload_file.read() # reading file for loading it in s3 storage
    await s3_client.upload_file(file, upload_file.filename)
    


@router.delete("{id}")
async def delete_mem(id: int):
    """Function for delete mem"""
    await BaseDAO.delete_mem_by_id(id)