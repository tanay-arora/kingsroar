# Generated by Django 3.2.5 on 2021-07-13 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_godown_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='godown',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.seller'),
        ),
    ]
