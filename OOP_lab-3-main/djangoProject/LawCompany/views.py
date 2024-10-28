from rest_framework import viewsets, status
from rest_framework.response import Response
from LawCompany.repositories.repository_Factory import RepositoryFactory
from LawCompany.serializers import *
from rest_framework.permissions import IsAuthenticated


class BaseViewSet(viewsets.ViewSet):
    repository = None
    serializer_class = None
    permission_classes = [IsAuthenticated]
    def get_repository(self):
        if not self.repository:
            raise NotImplementedError("Repository not provided")
        return self.repository

    def list(self, request):
        objects = self.get_repository().get_all()
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.get_repository().create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        obj = self.get_repository().get_by_id(pk)
        if obj:
            serializer = self.serializer_class(obj)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        obj = self.get_repository().get_by_id(pk)
        if obj:
            serializer = self.serializer_class(obj, data=request.data)
            if serializer.is_valid():
                self.get_repository().update(pk, **serializer.validated_data)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        success = self.get_repository().delete(pk)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)




class ClientViewSet(BaseViewSet):
    repository = RepositoryFactory.get_client_repository()
    serializer_class = ClientSerializer

class AttorneyViewSet(BaseViewSet):
    repository = RepositoryFactory.get_attorney_repository()
    serializer_class = AttorneySerializer

class SpecializationViewSet(BaseViewSet):
    repository = RepositoryFactory.get_specialization_repository()
    serializer_class = SpecializationSerializer

class AttorneySpecializationViewSet(BaseViewSet):
    repository = RepositoryFactory.get_attorney_specialization_repository()
    serializer_class = AttorneySpecializationSerializer

class CaseStatusViewSet(BaseViewSet):
    repository = RepositoryFactory.get_case_status_repository()
    serializer_class = CaseStatusSerializer

class CaseViewSet(BaseViewSet):
    repository = RepositoryFactory.get_case_repository()
    serializer_class = CaseSerializer

class PrecedentViewSet(BaseViewSet):
    repository = RepositoryFactory.get_precedent_repository()
    serializer_class = PrecedentSerializer

class CourtViewSet(BaseViewSet):
    repository = RepositoryFactory.get_court_repository()
    serializer_class = CourtSerializer

class JudgeViewSet(BaseViewSet):
    repository = RepositoryFactory.get_judge_repository()
    serializer_class = JudgeSerializer

class CaseCourtViewSet(BaseViewSet):
    repository = RepositoryFactory.get_case_court_repository()
    serializer_class = CaseCourtSerializer

class AppointmentViewSet(BaseViewSet):
    repository = RepositoryFactory.get_appointment_repository()
    serializer_class = AppointmentSerializer

class InvoiceViewSet(BaseViewSet):
    repository = RepositoryFactory.get_invoice_repository()
    serializer_class = InvoiceSerializer

class PaymentViewSet(BaseViewSet):
    repository = RepositoryFactory.get_payment_repository()
    serializer_class = PaymentSerializer

class DocumentViewSet(BaseViewSet):
    repository = RepositoryFactory.get_document_repository()
    serializer_class = DocumentSerializer

class AssistantViewSet(BaseViewSet):
    repository = RepositoryFactory.get_assistant_repository()
    serializer_class = AssistantSerializer
