# Generated by Django 2.2.1 on 2019-05-17 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_full_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
