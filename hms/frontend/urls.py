from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.get_home, name='get_home'),
    path('manage_doctor', views.get_doctor_manage, name='get_doctor_manage'),
    path('manage_employee', views.get_employee_manage, name='get_employee_manage'),
    path('add_employee', views.add_empl, name='add_empl'),
    path('edit_empl/<int:employee_id>/', views.edit_empl, name='edit_empl'),
    path('employees/delete/<int:employee_id>/', views.delete_empl, name='delete_empl'),

    path('patients/', views.get_patient_manage, name='get_patient_manage'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/edit/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('patients/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),

    path('clinics/', views.clinic_manage, name='clinic_manage'),  # Đường dẫn cho trang quản lý phòng khám
    path('clinics/add/', views.add_clinic, name='add_clinic'),  # Đường dẫn cho chức năng thêm phòng khám
    path('clinics/<int:clinic_id>/edit/', views.edit_clinic, name='edit_clinic'),  # Đường dẫn cho chức năng sửa phòng khám
    path('clinics/<int:clinic_id>/delete/', views.delete_clinic, name='delete_clinic'),  # Đường dẫn cho chức năng xóa phòng khám

    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/<int:appointment_id>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),

    path('medical-records/', views.medical_record_list, name='medical_record_list'),
    path('medical-records/add/', views.add_record, name='add_record'),
    path('medical-records/<int:record_id>/edit/', views.edit_record, name='edit_record'),
    path('medical-records/<int:record_id>/delete/', views.delete_record, name='delete_record'),
]

