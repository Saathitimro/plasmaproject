# Generated by Django 3.1.6 on 2021-05-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=50)),
                ('Contact', models.TextField(max_length=10)),
                ('Address', models.TextField(max_length=10)),
                ('Blood_type', models.TextField(max_length=10)),
                ('Vacinated', models.BooleanField()),
                ('Recovered', models.TextField(max_length=50)),
                ('Verify', models.BooleanField()),
            ],
        ),
    ]
