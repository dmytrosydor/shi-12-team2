from ..models  import Client
from .base_repository import BaseRepository
class ClientRepository(BaseRepository):
    model = Client

    def get_by_id(self, client_id):
        return self.model.objects.filter(ClientID=client_id).first()

    def update(self, client_id, **kwargs):
        client = self.get_by_id(client_id)
        if client:
            for key, value in kwargs.items():
                setattr(client, key, value)
            client.save()
            return client
        return None

    def delete(self, client_id):
        client = self.get_by_id(client_id)
        if client:
            client.delete()
            return True
        return False
