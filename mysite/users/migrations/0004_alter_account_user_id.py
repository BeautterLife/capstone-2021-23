# Generated by Django 3.2 on 2021-05-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_cam_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_id',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
