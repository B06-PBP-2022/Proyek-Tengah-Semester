# Generated by Django 4.1 on 2022-10-31 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastedited',
            name='password_edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lastedited',
            name='username_edited',
            field=models.BooleanField(default=False),
        ),
    ]
