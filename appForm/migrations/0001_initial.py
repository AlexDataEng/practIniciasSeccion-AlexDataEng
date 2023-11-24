# Generated by Django 4.2.7 on 2023-11-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Productos",
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
                ("codigo", models.IntegerField()),
                ("lote", models.IntegerField()),
                ("producto", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
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
                ("rut", models.CharField(max_length=12)),
                ("nombres", models.CharField(max_length=255)),
                ("contrasena", models.CharField(max_length=255)),
            ],
        ),
    ]
