# Generated by Django 3.1.6 on 2021-05-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasma', '0007_donor_recovered_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='Address',
            field=models.TextField(max_length=100),
        ),
    ]
