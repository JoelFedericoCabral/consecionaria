# Generated by Django 5.0.7 on 2024-10-16 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_alter_empleado_apellido_alter_empleado_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='autos/'),
        ),
    ]
