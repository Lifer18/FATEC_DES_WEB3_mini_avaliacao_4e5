# Generated by Django 4.1.1 on 2023-05-04 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_atividademodel_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividademodel',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 5, 4, 0, 26, 48, 562333, tzinfo=datetime.timezone.utc), verbose_name='Data'),
        ),
    ]
