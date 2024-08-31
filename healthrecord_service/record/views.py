import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

DOCTOR_SERVICE_URL = 'http://localhost:1301/api/doctors/'
PATIENT_SERVICE_URL = 'http://localhost:1303/api/patients/'

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    def retrieve_related_info(self, medical_record):
        # Retrieve doctor info
        doctor_response = requests.get(f"{DOCTOR_SERVICE_URL}{medical_record.doctor_id}/")
        doctor_info = doctor_response.json() if doctor_response.status_code == 200 else {}

        # Retrieve patient info
        patient_response = requests.get(f"{PATIENT_SERVICE_URL}{medical_record.patient_id}/")
        patient_info = patient_response.json() if patient_response.status_code == 200 else {}

        return doctor_info, patient_info

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            medical_record = MedicalRecord.objects.get(id=response.data['id'])
            doctor_info, patient_info = self.retrieve_related_info(medical_record)
            response.data['doctor_info'] = doctor_info
            response.data['patient_info'] = patient_info
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            medical_record = self.get_object()
            doctor_info, patient_info = self.retrieve_related_info(medical_record)
            response.data['doctor_info'] = doctor_info
            response.data['patient_info'] = patient_info
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            medical_record = self.get_object()
            doctor_info, patient_info = self.retrieve_related_info(medical_record)
            response.data['doctor_info'] = doctor_info
            response.data['patient_info'] = patient_info
        return response

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for record in response.data:
            medical_record = MedicalRecord.objects.get(id=record['id'])
            doctor_info, patient_info = self.retrieve_related_info(medical_record)
            record['doctor_info'] = doctor_info
            record['patient_info'] = patient_info
        return response
