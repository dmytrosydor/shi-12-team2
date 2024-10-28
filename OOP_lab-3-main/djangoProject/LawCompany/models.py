from django.db import models

class Client(models.Model):
    ClientID = models.AutoField(primary_key=True)
    ClientName = models.CharField(max_length=70)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=11)

    def __str__(self):
        return self.ClientName


class Attorney(models.Model):
    AttorneyID = models.AutoField(primary_key=True)
    AttorneyName = models.CharField(max_length=70)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=11)
    YearsOfExperience = models.IntegerField()

    def __str__(self):
        return self.AttorneyName


class Specialization(models.Model):
    SpecializationID = models.AutoField(primary_key=True)
    TypeSpecialization = models.CharField(max_length=50)

    def __str__(self):
        return self.TypeSpecialization


class AttorneySpecialization(models.Model):
    AttorneySpecializationID = models.AutoField(primary_key=True)
    Attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)
    Specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Attorney} - {self.Specialization}"


class CaseStatus(models.Model):
    StatusID = models.AutoField(primary_key=True)
    StatusDescription = models.CharField(max_length=50)

    def __str__(self):
        return self.StatusDescription


class Case(models.Model):
    CaseID = models.AutoField(primary_key=True)
    CaseType = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Status = models.ForeignKey(CaseStatus, on_delete=models.CASCADE)
    Attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.CaseType


class Precedent(models.Model):
    PrecedentID = models.AutoField(primary_key=True)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)
    PrecedentDescription = models.CharField(max_length=150)

    def __str__(self):
        return self.PrecedentDescription


class Court(models.Model):
    CourtID = models.AutoField(primary_key=True)
    CourtName = models.CharField(max_length=70)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.CourtName


class Judge(models.Model):
    JudgeID = models.AutoField(primary_key=True)
    JudgeName = models.CharField(max_length=70)
    Court = models.ForeignKey(Court, on_delete=models.CASCADE)
    YearsOfExperience = models.IntegerField()

    def __str__(self):
        return self.JudgeName


class CaseCourt(models.Model):
    CaseCourtID = models.AutoField(primary_key=True)
    Court = models.ForeignKey(Court, on_delete=models.CASCADE)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)
    Judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    HearingDate = models.DateField()

    def __str__(self):
        return f"{self.Case} at {self.Court}"


class Appointment(models.Model):
    AppointmentID = models.AutoField(primary_key=True)
    Date = models.DateField()
    Time = models.TimeField()
    Attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.Client} with {self.Attorney} on {self.Date}"


class Invoice(models.Model):
    InvoiceID = models.AutoField(primary_key=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    IssueDate = models.DateField()
    DueDate = models.DateField()
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice {self.InvoiceID} for {self.Client}"


class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    PaymentDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentMethod = models.CharField(max_length=50)
    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.PaymentID} for Invoice {self.Invoice}"


class Document(models.Model):
    DocumentID = models.AutoField(primary_key=True)
    FileName = models.CharField(max_length=150)
    UploadDate = models.DateField()
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return self.FileName


class Assistant(models.Model):
    AssistantID = models.AutoField(primary_key=True)
    AssistantName = models.CharField(max_length=70)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=11)
    Attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)

    def __str__(self):
        return self.AssistantName