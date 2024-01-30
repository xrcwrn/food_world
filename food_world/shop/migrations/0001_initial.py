# Generated by Django 5.0.1 on 2024-01-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=90)),
                ('item_name', models.CharField(max_length=90)),
                ('item_type', models.CharField(max_length=90)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('item_image', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=5)),
            ],
        ),
    ]
