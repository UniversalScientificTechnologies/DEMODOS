# Generated by Django 4.2.16 on 2024-11-25 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetectorUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_dose', models.FloatField(default=0.0)),
                ('random_values_enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('detailed_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('detailed_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dose', models.FloatField()),
                ('detector_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_data', to='demodos_ui.detectoruser')),
            ],
        ),
        migrations.AddField(
            model_name='detectoruser',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='demodos_ui.group'),
        ),
        migrations.AddField(
            model_name='detectoruser',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detectors', to='demodos_ui.location'),
        ),
    ]
