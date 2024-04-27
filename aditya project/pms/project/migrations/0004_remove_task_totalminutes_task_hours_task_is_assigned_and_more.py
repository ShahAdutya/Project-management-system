# Generated by Django 5.0.2 on 2024-03-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_projectmodule_task_usertask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='totalMinutes',
        ),
        migrations.AddField(
            model_name='task',
            name='hours',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='is_assigned',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='usertask',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectmodule',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterModelTable(
            name='usertask',
            table='user_task',
        ),
    ]
