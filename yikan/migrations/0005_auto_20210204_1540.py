# Generated by Django 3.1.5 on 2021-02-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yikan', '0004_auto_20210204_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateinfo',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
