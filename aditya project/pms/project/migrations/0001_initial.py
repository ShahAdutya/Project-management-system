# Generated by Django 5.0.2 on 2024-03-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(choices=[('python', 'python'), ('Java', 'Java'), ('C++', 'C++'), ('C#', 'C#')], max_length=100)),
                ('estimated_hours', models.PositiveBigIntegerField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
