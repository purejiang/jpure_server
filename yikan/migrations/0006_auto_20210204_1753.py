# Generated by Django 3.1.5 on 2021-02-04 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yikan', '0005_auto_20210204_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='updateinfo',
            old_name='sign_md5',
            new_name='app_sign',
        ),
    ]
