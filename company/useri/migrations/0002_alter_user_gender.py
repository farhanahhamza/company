# Generated by Django 4.2.5 on 2023-09-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=20),
        ),
    ]
