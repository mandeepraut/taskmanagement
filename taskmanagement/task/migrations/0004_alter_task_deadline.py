# Generated by Django 4.2.5 on 2024-02-15 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 16, 12, 42, 51, 952453)),
        ),
    ]
