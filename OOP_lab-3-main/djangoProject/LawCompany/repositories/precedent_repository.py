from ..models import Precedent
from .base_repository import BaseRepository

class PrecedentRepository(BaseRepository):
    model = Precedent

    def update(self, precedent_id, **kwargs):
        precedent = self.get_by_id(precedent_id)
        if precedent:
            for key, value in kwargs.items():
                setattr(precedent, key, value)
            precedent.save()
            return precedent
        return None

    def delete(self, precedent_id):
        precedent = self.get_by_id(precedent_id)
        if precedent:
            precedent.delete()
            return True
        return False
