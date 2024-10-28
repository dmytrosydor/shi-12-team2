from ..models import Appointment
from .base_repository import BaseRepository

class AppointmentRepository(BaseRepository):
    model = Appointment

    def update(self, appointment_id, **kwargs):
        appointment = self.get_by_id(appointment_id)
        if appointment:
            for key, value in kwargs.items():
                setattr(appointment, key, value)
            appointment.save()
            return appointment
        return None

    def delete(self, appointment_id):
        appointment = self.get_by_id(appointment_id)
        if appointment:
            appointment.delete()
            return True
        return False
