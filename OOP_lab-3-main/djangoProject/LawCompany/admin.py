from django.contrib import admin
from LawCompany.models import Attorney, Client, CaseStatus

admin.site.register(Attorney)
admin.site.register(Client)
admin.site.register(CaseStatus)