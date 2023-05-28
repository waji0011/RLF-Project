# Generated by Django 4.1.2 on 2023-05-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0045_alter_userdata_back_cnic_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='back_cnic_picture',
            field=models.ImageField(blank=True, null=True, upload_to='cnic_pictures'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='front_cnic_picture',
            field=models.ImageField(blank=True, null=True, upload_to='cnic_pictures'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]
