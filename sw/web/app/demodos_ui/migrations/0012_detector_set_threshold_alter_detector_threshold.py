# Generated by Django 4.2.16 on 2024-12-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demodos_ui', '0011_rename_set_threshold_detector_threshold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detector',
            name='set_threshold',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='detector',
            name='threshold',
            field=models.FloatField(default=0),
        ),
    ]
