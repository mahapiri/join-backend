# Generated by Django 5.1.7 on 2025-03-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_create_date_task_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, default='to_do', max_length=50),
        ),
    ]
