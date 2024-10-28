from rest_framework import serializers
from .models import Client, Attorney, Specialization, AttorneySpecialization, CaseStatus, Case, Precedent, Court, Judge, CaseCourt, Appointment, Invoice, Payment, Document, Assistant

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AttorneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Attorney
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class AttorneySpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttorneySpecialization
        fields = '__all__'

class CaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStatus
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class PrecedentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precedent
        fields = '__all__'

class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'

class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'

class CaseCourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseCourt
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'
