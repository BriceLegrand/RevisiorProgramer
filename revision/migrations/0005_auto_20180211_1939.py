# Generated by Django 2.0.2 on 2018-02-11 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision', '0004_auto_20180211_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabletime',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='availabletime',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='course',
            name='fifth_learning_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='first_learning_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='fourth_learning_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='second_learning_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='seen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='started_learning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='third_learning_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
