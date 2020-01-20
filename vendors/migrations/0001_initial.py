# Generated by Django 2.2.1 on 2019-05-17 13:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('bzname', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('purpose', models.IntegerField(blank=True, choices=[(1, 'Venue'), (2, 'Photographer'), (3, 'Florist'), (4, 'Cake'), (5, 'Catering'), (6, 'Clothing'), (7, 'Dj')])),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('facebook', models.CharField(blank=True, max_length=200)),
                ('twitter', models.CharField(blank=True, max_length=200)),
                ('instagram', models.CharField(blank=True, max_length=200)),
                ('youtube', models.CharField(blank=True, max_length=200)),
                ('reg_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]