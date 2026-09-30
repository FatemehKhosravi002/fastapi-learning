
from models import Note

class NoteService:
    def __init__(self, repository):
        self.repository = repository

    async def create_note(self , note):
        note_model = Note(
            title = note.title,
            description= note.description
        )

        return await self.repository.create_note(note_model)