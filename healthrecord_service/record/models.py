from django.db import models

class MedicalRecord(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    date = models.DateField()
    diagnosis = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Medical Record for Patient {self.patient_id} - {self.date}"
