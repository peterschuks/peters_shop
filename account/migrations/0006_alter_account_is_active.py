# Generated by Django 3.2.14 on 2023-03-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
