# Generated by Django 2.0.13 on 2019-03-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20190302_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]