# Generated by Django 5.0.2 on 2024-04-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
    ]
