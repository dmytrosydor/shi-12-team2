class BaseRepository:
    model = None

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, id):
        return self.model.objects.filter(id=id).first()

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        instance.save()
        return instance

    
