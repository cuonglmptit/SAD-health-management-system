import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

DOCTOR_SERVICE_URL = 'http://127.0.0.1:1301/api/doctors/'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Kiểm tra nếu vị trí là 'Doctor'
        if request.data.get('position') == 'Doctor':
            doctor_data = {
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'specialty': request.data.get('department'),
                'position' : request.data.get('position'),
                'phone_number': request.data.get('phone_number'),
                'email': request.data.get('email'),
                'address': request.data.get('address')
            }
            # Gửi yêu cầu POST đến service quản lý bác sĩ
            requests.post(DOCTOR_SERVICE_URL, data=doctor_data)
        else:
            new_employee = Employee(
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                date_of_birth=request.data.get('date_of_birth'),
                position=request.data.get('position'),
                department=request.data.get('department'),
                phone_number=request.data.get('phone_number'),
                email=request.data.get('email'),
                address=request.data.get('address')
            )
            new_employee.save
        return response

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        response = super().update(request, *args, **kwargs)
        # Kiểm tra nếu vị trí là 'Doctor'
        if instance.position == 'Doctor':
            doctor_id = self.get_doctor_id(instance.email)
            if doctor_id:
                doctor_data = {
                    'first_name': request.data.get('first_name'),
                    'last_name': request.data.get('last_name'),
                    'specialty': request.data.get('department'),
                     'position' : request.data.get('position'),
                    'phone_number': request.data.get('phone_number'),
                    'email': request.data.get('email'),
                    'address': request.data.get('address')
                }
                # Gửi yêu cầu PUT đến service quản lý bác sĩ
                requests.put(f"{DOCTOR_SERVICE_URL}{doctor_id}/", data=doctor_data)
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Kiểm tra nếu vị trí là 'Doctor'
        if instance.position == 'Doctor':
            doctor_id = self.get_doctor_id(instance.email)
            if doctor_id:
                # Gửi yêu cầu DELETE đến service quản lý bác sĩ
                requests.delete(f"{DOCTOR_SERVICE_URL}{doctor_id}/")
        return super().destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Gửi yêu cầu GET để lấy thông tin tất cả nhân viên
        employee_response = requests.get('http://127.0.0.1:8001/api/employees/')
        employees = employee_response.json() if employee_response.status_code == 200 else []

        # Gửi yêu cầu GET để lấy thông tin tất cả bác sĩ
        doctor_response = requests.get(DOCTOR_SERVICE_URL)
        doctors = doctor_response.json() if doctor_response.status_code == 200 else []

        # Kết hợp thông tin nhân viên và bác sĩ thành một danh sách
        all_staff = employees + doctors

        return Response(all_staff)
    
    def get_doctor_id(self, email):
        # Gửi yêu cầu GET để lấy thông tin tất cả bác sĩ
        doctor_response = requests.get(DOCTOR_SERVICE_URL)
        if doctor_response.status_code == 200:
            doctors = doctor_response.json()
            for doctor in doctors:
                if doctor['email'] == email:
                    return doctor['id']
        return None

