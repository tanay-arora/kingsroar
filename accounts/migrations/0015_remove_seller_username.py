# Generated by Django 3.2.5 on 2021-07-13 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210713_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='username',
        ),
    ]
