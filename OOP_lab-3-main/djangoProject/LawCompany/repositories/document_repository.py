from ..models import Document
from .base_repository import BaseRepository

class DocumentRepository(BaseRepository):
    model = Document

    def update(self, document_id, **kwargs):
        document = self.get_by_id(document_id)
        if document:
            for key, value in kwargs.items():
                setattr(document, key, value)
            document.save()
            return document
        return None

    def delete(self, document_id):
        document = self.get_by_id(document_id)
        if document:
            document.delete()
            return True
        return False
