# Generated by Django 3.2 on 2021-05-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cctv',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
