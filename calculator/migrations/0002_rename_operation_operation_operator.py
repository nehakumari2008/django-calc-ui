# Generated by Django 4.1.5 on 2023-01-04 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='Operation',
            new_name='operator',
        ),
    ]
