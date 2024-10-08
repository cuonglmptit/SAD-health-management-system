# Generated by Django 4.1.13 on 2024-05-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patient_name", models.IntegerField()),
                ("doctor_name", models.IntegerField()),
                ("clinic_id", models.IntegerField()),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("description", models.TextField()),
            ],
        ),
    ]
