# Generated by Django 3.2.2 on 2021-07-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210708_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='custdomer',
            field=models.BooleanField(default=False),
        ),
    ]