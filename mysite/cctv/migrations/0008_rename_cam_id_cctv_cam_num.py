# Generated by Django 3.2 on 2021-05-23 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0007_rename_file_name_record_file_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cctv',
            old_name='cam_id',
            new_name='cam_num',
        ),
    ]