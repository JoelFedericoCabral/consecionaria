# Generated by Django 5.0.7 on 2024-10-21 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_alter_auto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.categoria', verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='descripcion',
            field=models.TextField(verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='autos/', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.marca', verbose_name='marca'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.modeloauto', verbose_name='modelo'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='precio'),
        ),
    ]
