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



@router.post("/add_mem", status_code=201)
async def add_mem(upload_file: UploadFile):
    """Function for add mem in s3-storage and DB"""
    
    file =  await upload_file.read() # reading file for loading it in s3 storage
    await s3_client.upload_file(file, upload_file.filename) # add file in s3-storage

    # URL file from s3-storage
    url = f"https://98508f70-8b19-40be-83a5-86249d08e148.selstorage.ru/{upload_file.filename}"

    # add mem in DB whith name and url from s3-storage
    await BaseDAO.add_mem(name=upload_file.filename, url=url)

    


@router.delete("{id}")
async def delete_mem(id: int):
    """Function for delete mem"""
    await BaseDAO.delete_mem_by_id(id)