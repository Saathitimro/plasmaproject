# Generated by Django 3.1.6 on 2021-05-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasma', '0006_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='Recovered_time',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
