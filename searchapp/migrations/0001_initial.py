# Generated by Django 4.0.4 on 2022-04-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(default='SOME STRING', max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]