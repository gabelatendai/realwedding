# Generated by Django 2.2.1 on 2019-05-18 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20190518_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='address',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='city',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='country',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='zipcode',
        ),
    ]
