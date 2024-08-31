import subprocess

# Khởi động server cho project 1
subprocess.Popen(['python', 'hms/manage.py', 'runserver', '1300'])

# Khởi động server cho project 2
subprocess.Popen(['python', 'doctor_service/manage.py', 'runserver', '1301'])

# Khởi động server cho project 3
subprocess.Popen(['python', 'employee_service/manage.py', 'runserver', '1302'])

# Khởi động server cho project 4
subprocess.Popen(['python', 'patient_service/manage.py', 'runserver', '1303'])

# Khởi động server cho project 5
subprocess.Popen(['python', 'clinic_service/manage.py', 'runserver', '1304'])

# Khởi động server cho project 6
subprocess.Popen(['python', 'appointment_service/manage.py', 'runserver', '1305'])

# Khởi động server cho project 7
subprocess.Popen(['python', 'healthrecord_service/manage.py', 'runserver', '1306'])