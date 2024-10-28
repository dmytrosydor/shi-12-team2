from ..models import Court
from .base_repository import BaseRepository

class CourtRepository(BaseRepository):
    model = Court

    def update(self, court_id, **kwargs):
        court = self.get_by_id(court_id)
        if court:
            for key, value in kwargs.items():
                setattr(court, key, value)
            court.save()
            return court
        return None

    def delete(self, court_id):
        court = self.get_by_id(court_id)
        if court:
            court.delete()
            return True
        return False
