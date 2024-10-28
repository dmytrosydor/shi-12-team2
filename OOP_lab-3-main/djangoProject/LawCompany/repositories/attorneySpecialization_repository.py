from ..models import AttorneySpecialization
from .base_repository import BaseRepository

class AttorneySpecializationRepository(BaseRepository):
    model = AttorneySpecialization

    def update(self, attorney_specialization_id, **kwargs):
        attorney_specialization = self.get_by_id(attorney_specialization_id)
        if attorney_specialization:
            for key, value in kwargs.items():
                setattr(attorney_specialization, key, value)
            attorney_specialization.save()
            return attorney_specialization
        return None

    def delete(self, attorney_specialization_id):
        attorney_specialization = self.get_by_id(attorney_specialization_id)
        if attorney_specialization:
            attorney_specialization.delete()
            return True
        return False
