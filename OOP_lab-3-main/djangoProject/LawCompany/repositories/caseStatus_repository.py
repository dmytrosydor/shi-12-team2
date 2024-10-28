from ..models import CaseStatus
from .base_repository import BaseRepository

class CaseStatusRepository(BaseRepository):
    model = CaseStatus

    def update(self, status_id, **kwargs):
        status = self.get_by_id(status_id)
        if status:
            for key, value in kwargs.items():
                setattr(status, key, value)
            status.save()
            return status
        return None

    def delete(self, status_id):
        status = self.get_by_id(status_id)
        if status:
            status.delete()
            return True
        return False
