# Generated by Django 4.1.5 on 2023-01-04 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_rename_operation_operation_operator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='First_number',
        ),
        migrations.AlterField(
            model_name='operation',
            name='Created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 4, 11, 6, 37, 741541, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='operation',
            name='Second_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='operation',
            name='first_number',
            field=models.IntegerField(default=0),
        ),
    ]
