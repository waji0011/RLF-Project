# Generated by Django 4.1.2 on 2023-05-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_contact_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='has_submitted_registration_form',
            field=models.BooleanField(default=False),
        ),
    ]
