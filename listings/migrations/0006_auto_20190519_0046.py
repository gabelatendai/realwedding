# Generated by Django 2.2.1 on 2019-05-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20190518_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.IntegerField(),
        ),
    ]
