# Generated by Django 5.1.7 on 2025-03-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prio',
            field=models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('medium', 'Medium'), ('low', 'Low')], max_length=10, null=True),
        ),
    ]
