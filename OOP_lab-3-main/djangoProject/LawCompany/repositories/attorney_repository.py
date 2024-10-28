from ..models import Attorney
from .base_repository import BaseRepository

class AttorneyRepository(BaseRepository):
    model = Attorney

    def update(self, attorney_id, **kwargs):
        attorney = self.get_by_id(attorney_id)
        if attorney:
            for key, value in kwargs.items():
                setattr(attorney, key, value)
            attorney.save()
            return attorney
        return None



    def delete(self, attorney_id):
        attorney = self.get_by_id(attorney_id)
        if attorney:
            attorney.delete()
            return True
        return False
