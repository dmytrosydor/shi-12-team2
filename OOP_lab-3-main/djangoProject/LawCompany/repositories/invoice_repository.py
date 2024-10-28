from ..models import Invoice
from .base_repository import BaseRepository

class InvoiceRepository(BaseRepository):
    model = Invoice

    def update(self, invoice_id, **kwargs):
        invoice = self.get_by_id(invoice_id)
        if invoice:
            for key, value in kwargs.items():
                setattr(invoice, key, value)
            invoice.save()
            return invoice
        return None

    def delete(self, invoice_id):
        invoice = self.get_by_id(invoice_id)
        if invoice:
            invoice.delete()
            return True
        return False
