# Generated by Django 4.1.2 on 2023-05-10 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_rename_has_submitted_challan_profile_has_submitted_challan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='challan',
            name='verified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
