from fastapi import APIRouter, Depends
from services import NoteService
from dependencies import CreateService
from schemas import CreateNote


router = APIRouter(
    prefix="/note"
)


@router.post("/create")
async def create_note(note: CreateNote,
                      service: NoteService = Depends(CreateService)):
    return await service.create_note(note)