from sqlalchemy import delete, insert, select
from app.database import async_session_maker
from app.dbmodel import Mems


class BaseDAO:

    @classmethod
    async def get_all(cls):
        """Method for find all mems"""

        async with async_session_maker() as session:
            query = select(Mems.name, Mems.url)
            mems = await session.execute(query)
            return mems.mappings().all()
        
    
    @classmethod
    async def get_mem_by_id(cls, mem_id : int):
        """Method for find mem by id"""

        async with async_session_maker() as session:
            query = select(Mems.name, Mems.url).filter_by(id = mem_id)
            mem = await session.execute(query)
            return mem.mappings().one_or_none()
        

    @classmethod
    async def delete_mem_by_id(cls, mem_id : int):
        """Method for delete mem by id"""

        async with async_session_maker() as session:
            query = delete(Mems).filter_by(id = mem_id)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def add_mem(cls, **data):
        """Method for add mem"""

        async with async_session_maker() as session:
            query = insert(Mems).values(**data)
            await session.execute(query)
            await session.commit()