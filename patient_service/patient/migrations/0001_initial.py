# Generated by Django 4.1.13 on 2024-05-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("address", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
