from .models import Appointment
from .serializers import AppointmentSerializer
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response



DOCTOR_SERVICE_URL = 'http://localhost:1301/api/doctors/'
PATIENT_SERVICE_URL = 'http://localhost:1303/api/patients/'
CLINIC_SERVICE_URL = 'http://localhost:1304/api/clinics/'
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    def retrieve_related_info(self, appointment):
        # Retrieve doctor info
        doctor_response = requests.get(f"{DOCTOR_SERVICE_URL}{appointment.doctor_id}/")
        doctor_info = doctor_response.json() if doctor_response.status_code == 200 else {}

        # Retrieve patient info
        patient_response = requests.get(f"{PATIENT_SERVICE_URL}{appointment.patient_id}/")
        patient_info = patient_response.json() if patient_response.status_code == 200 else {}

        clinic_response = requests.get(f"{CLINIC_SERVICE_URL}{appointment.clinic_id}/")
        clinic_info = clinic_response.json() if clinic_response.status_code == 200 else {}

        return doctor_info, patient_info, clinic_info
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            appointment = Appointment.objects.get(id=response.data['id'])
            doctor_info, patient_info, clinic_info = self.retrieve_related_info(appointment)
            response.data['doctor_info'] = doctor_info
            response.data['patient_info'] = patient_info
            response.data['clinic_info'] = clinic_info
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            appointment = self.get_object()
            doctor_info, patient_info,clinic_info = self.retrieve_related_info(appointment)
            response.data['doctor_info'] = doctor_info
            response.data['patient_info'] = patient_info
            response.data['clinic_info'] = clinic_info
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            appointment = self.get_object()
            doctor_info, patient_info,clinic_info = self.retrieve_related_info(appointment)
            response.data['doctor_info'] = doctor_info
            response.data['patient_info'] = patient_info
            response.data['clinic_info'] = clinic_info
        return response
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for record in response.data:
            appointment = Appointment.objects.get(id=record['id'])
            doctor_info, patient_info, clinic_info = self.retrieve_related_info(appointment)
            record['doctor_info'] = doctor_info
            record['patient_info'] = patient_info
            record['clinic_info'] = clinic_info
        return response
