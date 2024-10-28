from ..models import CaseCourt
from .base_repository import BaseRepository

class CaseCourtRepository(BaseRepository):
    model = CaseCourt

    def update(self, case_court_id, **kwargs):
        case_court = self.get_by_id(case_court_id)
        if case_court:
            for key, value in kwargs.items():
                setattr(case_court, key, value)
            case_court.save()
            return case_court
        return None

    def delete(self, case_court_id):
        case_court = self.get_by_id(case_court_id)
        if case_court:
            case_court.delete()
            return True
        return False
