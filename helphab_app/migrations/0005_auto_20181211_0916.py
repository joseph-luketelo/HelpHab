# Generated by Django 2.1.3 on 2018-12-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helphab_app', '0004_auto_20181210_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
