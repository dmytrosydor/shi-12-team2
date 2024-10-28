from ..models import Payment
from .base_repository import BaseRepository

class PaymentRepository(BaseRepository):
    model = Payment

    def update(self, payment_id, **kwargs):
        payment = self.get_by_id(payment_id)
        if payment:
            for key, value in kwargs.items():
                setattr(payment, key, value)
            payment.save()
            return payment
        return None

    def delete(self, payment_id):
        payment = self.get_by_id(payment_id)
        if payment:
            payment.delete()
            return True
        return False
