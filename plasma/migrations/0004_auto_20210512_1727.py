# Generated by Django 3.1.6 on 2021-05-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasma', '0003_auto_20210512_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='Verify',
            field=models.BooleanField(null=True),
        ),
    ]