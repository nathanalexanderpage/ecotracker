# Generated by Django 2.2.1 on 2019-08-18 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		('FuelTrackerApp', '0003_auto_20190818_1744'),
	]

	operations = [
		migrations.RemoveField(
			model_name='receipt',
			name='receipt_date',
		),
		migrations.RemoveField(
			model_name='receipt',
			name='receipt_time',
		),
		migrations.AddField(
			model_name='receipt',
			name='receipt_datetime',
			field=models.DateTimeField(default=datetime.datetime.now),
		),
	]
