# Generated by Django 2.2.1 on 2019-05-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20190517_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='purpose',
            field=models.IntegerField(choices=[(1, 'Venue'), (2, 'Photographer'), (3, 'Florist'), (4, 'Cake'), (5, 'Catering'), (6, 'Clothing'), (7, 'Dj')], default=1),
        ),
    ]