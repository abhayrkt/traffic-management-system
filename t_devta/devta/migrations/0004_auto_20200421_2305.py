# Generated by Django 3.0.4 on 2020-04-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devta', '0003_enquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='p_no',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='subject',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
