# Generated by Django 4.2.2 on 2023-07-08 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CraftifyApp', '0004_login_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='status',
        ),
    ]
