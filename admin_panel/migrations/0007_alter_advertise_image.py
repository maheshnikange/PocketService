# Generated by Django 5.0.4 on 2024-05-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_rename_name_advertise_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='image',
            field=models.ImageField(upload_to='uploads/advertise_images/'),
        ),
    ]
