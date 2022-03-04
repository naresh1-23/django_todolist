# Generated by Django 3.1 on 2022-03-04 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100000)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]