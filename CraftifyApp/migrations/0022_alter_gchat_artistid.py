# Generated by Django 5.0.1 on 2024-03-25 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftifyApp', '0021_gchat_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gchat',
            name='artistid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CraftifyApp.artist'),
        ),
    ]
