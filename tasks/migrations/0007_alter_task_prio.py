# Generated by Django 5.1.7 on 2025-03-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_prio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prio',
            field=models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('medium', 'Medium'), ('low', 'Low')], default='low', max_length=10, null=True),
        ),
    ]
