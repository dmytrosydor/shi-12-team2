from LawCompany.repositories.client_repository import ClientRepository
from LawCompany.repositories.attorney_repository import AttorneyRepository
from LawCompany.repositories.specialization_repository import SpecializationRepository
from LawCompany.repositories.attorneySpecialization_repository import AttorneySpecializationRepository
from LawCompany.repositories.caseStatus_repository import CaseStatusRepository
from LawCompany.repositories.case_repository import CaseRepository
from LawCompany.repositories.precedent_repository import PrecedentRepository
from LawCompany.repositories.court_repository import CourtRepository
from LawCompany.repositories.judge_repository import JudgeRepository
from LawCompany.repositories.caseCourt_repository import CaseCourtRepository
from LawCompany.repositories.appointment_repository import AppointmentRepository
from LawCompany.repositories.invoice_repository import InvoiceRepository
from LawCompany.repositories.payment_repository import PaymentRepository
from LawCompany.repositories.document_repository import DocumentRepository
from LawCompany.repositories.assistant_repository import AssistantRepository


class RepositoryFactory:
    @staticmethod
    def get_client_repository():
        return ClientRepository()

    @staticmethod
    def get_attorney_repository():
        return AttorneyRepository()

    @staticmethod
    def get_specialization_repository():
        return SpecializationRepository()

    @staticmethod
    def get_attorney_specialization_repository():
        return AttorneySpecializationRepository()

    @staticmethod
    def get_case_status_repository():
        return CaseStatusRepository()

    @staticmethod
    def get_case_repository():
        return CaseRepository()

    @staticmethod
    def get_precedent_repository():
        return PrecedentRepository()

    @staticmethod
    def get_court_repository():
        return CourtRepository()

    @staticmethod
    def get_judge_repository():
        return JudgeRepository()

    @staticmethod
    def get_case_court_repository():
        return CaseCourtRepository()

    @staticmethod
    def get_appointment_repository():
        return AppointmentRepository()

    @staticmethod
    def get_invoice_repository():
        return InvoiceRepository()

    @staticmethod
    def get_payment_repository():
        return PaymentRepository()

    @staticmethod
    def get_document_repository():
        return DocumentRepository()

    @staticmethod
    def get_assistant_repository():
        return AssistantRepository()
