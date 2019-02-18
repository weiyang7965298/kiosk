# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-18 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('completed_time', models.DateTimeField(null=True)),
                ('real_completed_time', models.DateTimeField(null=True)),
                ('checkin_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('access_token', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('refresh_token', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('token_expires_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irst_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('ssn', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WaitTime',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('wait_time', models.IntegerField(null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drchrono.Appointment')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drchrono.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drchrono.Patient'),
        ),
    ]
