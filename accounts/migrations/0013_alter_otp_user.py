# Generated by Django 3.2.5 on 2021-07-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_otp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='user',
            field=models.CharField(max_length=13),
        ),
    ]