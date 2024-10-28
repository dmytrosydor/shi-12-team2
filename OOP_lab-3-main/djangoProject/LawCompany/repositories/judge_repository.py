from ..models import Judge
from .base_repository import BaseRepository

class JudgeRepository(BaseRepository):
    model = Judge

    def update(self, judge_id, **kwargs):
        judge = self.get_by_id(judge_id)
        if judge:
            for key, value in kwargs.items():
                setattr(judge, key, value)
            judge.save()
            return judge
        return None

    def delete(self, judge_id):
        judge = self.get_by_id(judge_id)
        if judge:
            judge.delete()
            return True
        return False
