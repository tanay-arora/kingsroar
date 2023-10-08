# Generated by Django 3.2.5 on 2021-07-14 10:00

from django.db import migrations, models
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_godown_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='godown',
            name='gst_certificate',
            field=models.ImageField(upload_to='users/gst_certificates/', validators=[home.validators.clean_image]),
        ),
        migrations.AlterField(
            model_name='seller',
            name='pancard_image',
            field=models.ImageField(upload_to='users/pancards/', validators=[home.validators.clean_image]),
        ),
    ]