from ..models import Case, CaseStatus, Attorney, Client
from .base_repository import BaseRepository

class CaseRepository(BaseRepository):
    model = Case

    def update(self, case_id, **kwargs):
        case = self.get_by_id(case_id)
        if case:
            for key, value in kwargs.items():
                setattr(case, key, value)
            case.save()
            return case
        return None




    def delete(self, case_id):
        case = self.get_by_id(case_id)
        if case:
            case.delete()
            return True
        return False
