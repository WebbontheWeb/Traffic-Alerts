# Generated by Django 4.0 on 2021-12-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='fromAddress',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trip',
            name='toAddress',
            field=models.CharField(max_length=100),
        ),
    ]
