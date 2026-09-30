from models import Note



class NoteRepository:
    def __init__(self, session):
        self.session = session

    async def create_note(self, note:Note):
        self.session.add(note)
        await self.session.commit()
        return note