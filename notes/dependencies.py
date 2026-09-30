from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database import SessionFactory
from repository import NoteRepository
from services import NoteService

async def CreateSession():
    async with SessionFactory() as session:
        yield session

async def CreateRepository(session: AsyncSession = Depends(CreateSession)):
    return NoteRepository(session)

async def CreateService(repository: NoteRepository = Depends(CreateRepository)):
    return NoteService(repository)