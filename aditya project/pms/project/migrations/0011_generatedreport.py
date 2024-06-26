# Generated by Django 5.0.2 on 2024-03-30 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_alter_project_enddate_alter_project_startdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('completion_date', models.DateField()),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.task')),
            ],
        ),
    ]
