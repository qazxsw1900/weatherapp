# Generated by Django 4.0 on 2021-12-09 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 9, 19, 58, 56, 782902)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='note_content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='note_header',
            field=models.CharField(default='', max_length=128),
        ),
    ]