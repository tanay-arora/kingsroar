# Generated by Django 3.2.5 on 2021-07-13 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_seller_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='godown',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.seller'),
        ),
    ]
