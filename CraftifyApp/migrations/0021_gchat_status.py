# Generated by Django 5.0.1 on 2024-03-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftifyApp', '0020_alter_gchat_artistid'),
    ]

    operations = [
        migrations.AddField(
            model_name='gchat',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
