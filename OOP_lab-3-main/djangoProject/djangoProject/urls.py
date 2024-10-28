from django.urls import path, include
from rest_framework.routers import DefaultRouter
from LawCompany.views import *

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'attorneys', AttorneyViewSet, basename='attorney')
router.register(r'specializations', SpecializationViewSet, basename='specialization')
router.register(r'attorney_specializations', AttorneySpecializationViewSet, basename='attorney_specialization')
router.register(r'case_statuses', CaseStatusViewSet, basename='case_status')
router.register(r'cases', CaseViewSet, basename='case')
router.register(r'precedents', PrecedentViewSet, basename='precedent')
router.register(r'courts', CourtViewSet, basename='court')
router.register(r'judges', JudgeViewSet, basename='judge')
router.register(r'case_courts', CaseCourtViewSet, basename='case_court')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'assistants', AssistantViewSet, basename='assistant')

urlpatterns = [
    path('', include(router.urls)),
]
