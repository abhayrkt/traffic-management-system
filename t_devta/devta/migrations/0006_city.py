# Generated by Django 3.0.4 on 2020-04-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devta', '0005_challan_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
