# Generated by Django 5.0.1 on 2024-01-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ageRange',
            field=models.CharField(default='20-40', max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobileNo',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
