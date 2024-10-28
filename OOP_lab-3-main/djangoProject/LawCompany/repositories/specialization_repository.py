from ..models import Specialization
from .base_repository import BaseRepository

class SpecializationRepository(BaseRepository):
    model = Specialization

    def update(self, specialization_id, **kwargs):
        specialization = self.get_by_id(specialization_id)
        if specialization:
            for key, value in kwargs.items():
                setattr(specialization, key, value)
            specialization.save()
            return specialization
        return None

    def delete(self, specialization_id):
        specialization = self.get_by_id(specialization_id)
        if specialization:
            specialization.delete()
            return True
        return False
