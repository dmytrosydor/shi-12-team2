from ..models import Assistant
from .base_repository import BaseRepository

class AssistantRepository(BaseRepository):
    model = Assistant

    def update(self, assistant_id, **kwargs):
        assistant = self.get_by_id(assistant_id)
        if assistant:
            for key, value in kwargs.items():
                setattr(assistant, key, value)
            assistant.save()
            return assistant
        return None

    def delete(self, assistant_id):
        assistant = self.get_by_id(assistant_id)
        if assistant:
            assistant.delete()
            return True
        return False
