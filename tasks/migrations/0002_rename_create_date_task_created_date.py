# Generated by Django 5.1.7 on 2025-03-12 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
