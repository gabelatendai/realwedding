# Generated by Django 2.2.1 on 2019-05-18 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20190518_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='description',
            new_name='list_description',
        ),
    ]
