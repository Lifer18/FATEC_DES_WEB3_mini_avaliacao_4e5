# Generated by Django 4.1.9 on 2023-05-06 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_atividademodel_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividademodel',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 5, 6, 20, 44, 18, 415517, tzinfo=datetime.timezone.utc), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='atividademodel',
            name='descricao',
            field=models.CharField(blank=True, max_length=500, verbose_name='Descricao'),
        ),
    ]
