# Generated by Django 4.1.13 on 2024-05-31 16:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointment",
            old_name="doctor_name",
            new_name="doctor_id",
        ),
        migrations.RenameField(
            model_name="appointment",
            old_name="patient_name",
            new_name="patient_id",
        ),
    ]
