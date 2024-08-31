from django.shortcuts import render
from django.http import HttpResponse
from . models import *
import requests
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.urls import reverse
# Create your views here.

DOCTOR_SERVICE_URL = 'http://127.0.0.1:1301/api/doctors/'
EMPLOYEE_SERVICE_URL = 'http://127.0.0.1:1302/api/employees/'
PATIENT_SERVICE_URL = 'http://127.0.0.1:1303/api/patients/'
CLINIC_SERVICE_URL = 'http://127.0.0.1:1304/api/clinics/'
APPOINTMENT_SERVICE_URL = 'http://127.0.0.1:1305/api/appointments/'
HEALTHRECORD_SERVICE_URL = 'http://127.0.0.1:1306/api/medical-records/'



def get_home(request):
    context = {
        
    }
    return render(request=request, template_name='main.html', context=context)

def get_doctor_manage(request):
    context = {
        
    }
    return render(request=request, template_name='doctor.html', context=context)

def get_employee_manage(request):
    response = requests.get(EMPLOYEE_SERVICE_URL)
    if response.status_code == 200:
        employees = response.json()
    else:
        employees = []
    # print(employees)
    context = {
        'employees': employees
    }
    return render(request=request, template_name='employee.html', context=context)

def add_empl(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        position = request.POST.get('position')
        department = request.POST.get('department')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        # Gửi yêu cầu POST đến service employee
        response = requests.post(EMPLOYEE_SERVICE_URL, data={
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'position': position,
            'department': department,
            'phone_number': phone_number,
            'email': email,
            'address': address
        })
        
        # Kiểm tra kết quả trả về từ service employee
        if response.status_code == 201:
            # Nếu thành công, redirect về trang quản lý nhân viên
            return redirect(reverse('get_employee_manage'))
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        # Nếu request không phải là POST, hiển thị form để người dùng điền thông tin
        return render(request, 'employee_add.html')
    

def edit_empl(request, employee_id):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        position = request.POST.get('position')
        department = request.POST.get('department')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        # Gửi yêu cầu PUT đến service employee
        response = requests.put(f'{EMPLOYEE_SERVICE_URL}{employee_id}/', data={
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'position': position,
            'department': department,
            'phone_number': phone_number,
            'email': email,
            'address': address
        })
        
        # Kiểm tra kết quả trả về từ service employee
        if response.status_code == 200:
            # Nếu thành công, redirect về trang quản lý nhân viên
            return redirect(reverse('get_employee_manage'))
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        # Nếu request không phải là POST, hiển thị form để người dùng điền thông tin
        employee_response = requests.get(f'{EMPLOYEE_SERVICE_URL}{employee_id}/')
        if employee_response.status_code == 200:
            employee = employee_response.json()
        else:
            # Xử lý khi không thể lấy thông tin nhân viên
            pass
        return render(request, 'employee_edit.html', {'employee': employee})

def delete_empl(request, employee_id):
    if request.method == 'POST':
        response = requests.delete(f'{EMPLOYEE_SERVICE_URL}{employee_id}/')
        
        if response.status_code == 204:
            return redirect(reverse('get_employee_manage'))
        else:
            pass
    else:
        return redirect(reverse('get_employee_manage'))
    

def get_patient_manage(request):
    response = requests.get(PATIENT_SERVICE_URL)
    if response.status_code == 200:
        patients = response.json()
    else:
        patients = []
    context = {
        'patients': patients
    }
    return render(request=request, template_name='patient.html', context=context)

def add_patient(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        
        response = requests.post(PATIENT_SERVICE_URL, data={
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'address': address,
            'phone_number': phone_number,
            'email': email
        })
        
        if response.status_code == 201:
            return redirect(reverse('get_patient_manage'))
        else:
            pass
    else:
        return render(request, 'patient_add.html')

def edit_patient(request, patient_id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        
        response = requests.put(f'{PATIENT_SERVICE_URL}{patient_id}/', data={
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'address': address,
            'phone_number': phone_number,
            'email': email
        })
        
        if response.status_code == 200:
            return redirect(reverse('get_patient_manage'))
        else:
            pass
    else:
        patient_response = requests.get(f'{PATIENT_SERVICE_URL}{patient_id}/')
        if patient_response.status_code == 200:
            patient = patient_response.json()
        else:
            patient = None
        return render(request, 'patient_edit.html', {'patient': patient})
    
def delete_patient(request, patient_id):
    response = requests.delete(f'{PATIENT_SERVICE_URL}{patient_id}/')
    if response.status_code == 204:
        return redirect(reverse('get_patient_manage'))
    else:
        pass


def clinic_manage(request):
    response = requests.get(CLINIC_SERVICE_URL)
    if response.status_code == 200:
        clinics = response.json()
    else:
        clinics = []
    context = {
        'clinics': clinics
    }
    return render(request, 'clinic.html', context)

def add_clinic(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        name = request.POST.get('name')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        department = request.POST.get('department')
        clinic_type = request.POST.get('clinic_type')
        status = request.POST.get('status')

        # Gửi yêu cầu POST đến service phòng khám
        response = requests.post(CLINIC_SERVICE_URL, data={
            'name': name,
            'location': location,
            'phone_number': phone_number,
            'email': email,
            'department': department,
            'clinic_type': clinic_type,
            'status': status
        })
        
        # Kiểm tra kết quả trả về từ service phòng khám
        if response.status_code == 201:
            # Nếu thành công, redirect về trang quản lý phòng khám
            return redirect('clinic_manage')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        return render(request, 'clinic_add.html')

def edit_clinic(request, clinic_id):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        name = request.POST.get('name')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        department = request.POST.get('department')
        clinic_type = request.POST.get('clinic_type')
        status = request.POST.get('status')

        # Gửi yêu cầu PUT đến service phòng khám
        response = requests.put(f'{CLINIC_SERVICE_URL}{clinic_id}/', data={
            'name': name,
            'location': location,
            'phone_number': phone_number,
            'email': email,
            'department': department,
            'clinic_type': clinic_type,
            'status': status
        })
        
        # Kiểm tra kết quả trả về từ service phòng khám
        if response.status_code == 200:
            # Nếu thành công, redirect về trang quản lý phòng khám
            return redirect('clinic_manage')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        clinic_response = requests.get(f'{CLINIC_SERVICE_URL}{clinic_id}/')
        if clinic_response.status_code == 200:
            clinic = clinic_response.json()
        else:
            # Xử lý khi không thể lấy thông tin phòng khám
            pass
        return render(request, 'clinic_edit.html', {'clinic': clinic})

def delete_clinic(request, clinic_id):
    if request.method == 'POST':
        # Gửi yêu cầu DELETE đến service phòng khám
        response = requests.delete(f'{CLINIC_SERVICE_URL}{clinic_id}/')
        
        # Kiểm tra kết quả trả về từ service phòng khám
        if response.status_code == 204:
            # Nếu thành công, redirect về trang quản lý phòng khám
            return redirect('clinic_manage')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass

def appointment_list(request):
    # Gửi yêu cầu GET đến API
    response = requests.get(APPOINTMENT_SERVICE_URL)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        appointments = response.json()
        return render(request, 'appointment.html', {'appointments': appointments})
    else:
        # Xử lý trường hợp yêu cầu thất bại
        return render(request, 'error.html', {'message': 'Failed to fetch appointments'})
    
def add_appointment(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')
        clinic_id = request.POST.get('clinic_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        
        # Gửi yêu cầu POST đến service appointment
        response = requests.post(APPOINTMENT_SERVICE_URL, data={
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'clinic_id': clinic_id,
            'date': date,
            'time': time,
            'description': description
        })
        
        # Kiểm tra kết quả trả về từ service appointment
        if response.status_code == 201:
            # Nếu thành công, redirect về trang danh sách cuộc hẹn
            return redirect('appointment_list')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        # Nếu request không phải là POST, hiển thị form để người dùng điền thông tin
        # Lấy danh sách bệnh nhân, bác sĩ và phòng khám để hiển thị trong các dropdown list
        patient_response = requests.get(PATIENT_SERVICE_URL)
        doctor_response = requests.get(DOCTOR_SERVICE_URL)
        clinic_response = requests.get(CLINIC_SERVICE_URL)
        
        if patient_response.status_code == 200:
            patients = patient_response.json()
        else:
            patients = []
            
        if doctor_response.status_code == 200:
            doctors = doctor_response.json()
        else:
            doctors = []
            
        if clinic_response.status_code == 200:
            clinics = clinic_response.json()
        else:
            clinics = []
        
        return render(request, 'appointment_add.html', {'patients': patients, 'doctors': doctors, 'clinics': clinics})


def edit_appointment(request, appointment_id):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')
        clinic_id = request.POST.get('clinic_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        
        # Gửi yêu cầu PUT đến service appointment
        response = requests.put(f'{APPOINTMENT_SERVICE_URL}{appointment_id}/', data={
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'clinic_id': clinic_id,
            'date': date,
            'time': time,
            'description': description
        })
        
        # Kiểm tra kết quả trả về từ service appointment
        if response.status_code == 200:
            # Nếu thành công, redirect về trang danh sách cuộc hẹn
            return redirect('appointment_list')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        # Nếu request không phải là POST, hiển thị form để người dùng điều chỉnh thông tin
        appointment_response = requests.get(f'{APPOINTMENT_SERVICE_URL}{appointment_id}/')
        if appointment_response.status_code == 200:
            appointment = appointment_response.json()
        else:
            # Xử lý khi không thể lấy thông tin cuộc hẹn
            pass
        
        # Lấy danh sách bệnh nhân, bác sĩ và phòng khám để hiển thị trong các dropdown list
        patient_response = requests.get(PATIENT_SERVICE_URL)
        doctor_response = requests.get(DOCTOR_SERVICE_URL)
        clinic_response = requests.get(CLINIC_SERVICE_URL)
        
        if patient_response.status_code == 200:
            patients = patient_response.json()
        else:
            patients = []
            
        if doctor_response.status_code == 200:
            doctors = doctor_response.json()
        else:
            doctors = []
            
        if clinic_response.status_code == 200:
            clinics = clinic_response.json()
        else:
            clinics = []
        
        return render(request, 'appointment_edit.html', {'appointment': appointment, 'patients': patients, 'doctors': doctors, 'clinics': clinics})


def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        # Gửi yêu cầu DELETE đến service appointment
        response = requests.delete(f'{APPOINTMENT_SERVICE_URL}{appointment_id}/')
        
        # Kiểm tra kết quả trả về từ service appointment
        if response.status_code == 204:
            # Nếu thành công, redirect về trang danh sách cuộc hẹn
            return redirect('appointment_list')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        return redirect('appointment_list')
    

def medical_record_list(request):
    # Gửi yêu cầu GET đến API để lấy danh sách bản ghi y khoa
    response = requests.get(HEALTHRECORD_SERVICE_URL)
    if response.status_code == 200:
        medical_records = response.json()
    else:
        medical_records = []

    # Trả về trang HTML với danh sách bản ghi y khoa
    return render(request, 'record.html', {'medical_records': medical_records})


def add_record(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')
        date = request.POST.get('date')
        diagnosis = request.POST.get('diagnosis')
        prescription = request.POST.get('prescription')
        
        # Gửi yêu cầu POST đến service record
        response = requests.post(HEALTHRECORD_SERVICE_URL, data={
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'date': date,
            'diagnosis': diagnosis,
            'prescription': prescription
        })
        
        # Kiểm tra kết quả trả về từ service record
        if response.status_code == 201:
            # Nếu thành công, redirect về trang danh sách bản ghi y tế
            return redirect('medical_record_list')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        # Nếu request không phải là POST, hiển thị form để người dùng điền thông tin
        # Lấy danh sách bệnh nhân và bác sĩ để hiển thị trong các dropdown list
        patient_response = requests.get(PATIENT_SERVICE_URL)
        doctor_response = requests.get(DOCTOR_SERVICE_URL)
        
        if patient_response.status_code == 200:
            patients = patient_response.json()
        else:
            patients = []
            
        if doctor_response.status_code == 200:
            doctors = doctor_response.json()
        else:
            doctors = []
        
        return render(request, 'record_add.html', {'patients': patients, 'doctors': doctors})
    
def edit_record(request, record_id):
    if request.method == 'POST':
        # Lấy dữ liệu từ request
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')
        date = request.POST.get('date')
        diagnosis = request.POST.get('diagnosis')
        prescription = request.POST.get('prescription')
        
        # Gửi yêu cầu PUT đến service record
        response = requests.put(f'{HEALTHRECORD_SERVICE_URL}{record_id}/', data={
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'date': date,
            'diagnosis': diagnosis,
            'prescription': prescription
        })
        
        # Kiểm tra kết quả trả về từ service record
        if response.status_code == 200:
            # Nếu thành công, redirect về trang danh sách bản ghi y tế
            return redirect('medical_record_list')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        # Nếu request không phải là POST, hiển thị form để người dùng điều chỉnh thông tin
        record_response = requests.get(f'{HEALTHRECORD_SERVICE_URL}{record_id}/')
        if record_response.status_code == 200:
            record = record_response.json()
        else:
            # Xử lý khi không thể lấy thông tin bản ghi y tế
            pass
        
        # Lấy danh sách bệnh nhân và bác sĩ để hiển thị trong các dropdown list
        patient_response = requests.get(PATIENT_SERVICE_URL)
        doctor_response = requests.get(DOCTOR_SERVICE_URL)
        
        if patient_response.status_code == 200:
            patients = patient_response.json()
        else:
            patients = []
            
        if doctor_response.status_code == 200:
            doctors = doctor_response.json()
        else:
            doctors = []
        
        return render(request, 'record_edit.html', {'record': record, 'patients': patients, 'doctors': doctors})


def delete_record(request, record_id):
    if request.method == 'POST':
        # Gửi yêu cầu DELETE đến service record
        response = requests.delete(f'{HEALTHRECORD_SERVICE_URL}{record_id}/')
        
        # Kiểm tra kết quả trả về từ service record
        if response.status_code == 204:
            # Nếu thành công, redirect về trang danh sách bản ghi y tế
            return redirect('medical_record_list')
        else:
            # Nếu không thành công, xử lý theo yêu cầu của bạn
            pass
    else:
        return redirect('medical_record_list')
