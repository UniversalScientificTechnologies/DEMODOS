# Generated by Django 4.2.16 on 2024-12-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demodos_ui', '0005_rename_battery_status_device_battery_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='charging_status',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
