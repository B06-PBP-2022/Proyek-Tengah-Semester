# Generated by Django 4.1 on 2022-10-28 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_carbonkendaraandarat_date_input_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbonkendaraandarat',
            name='date_input',
            field=models.DateField(default=datetime.date(2022, 10, 28)),
        ),
        migrations.AlterField(
            model_name='carbonlistrik',
            name='date_input',
            field=models.DateField(default=datetime.date(2022, 10, 28)),
        ),
    ]