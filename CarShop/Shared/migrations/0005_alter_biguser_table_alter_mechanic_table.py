# Generated by Django 4.2.5 on 2023-09-19 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shared', '0004_mechanic_biguser'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='biguser',
            table='shared_big_user',
        ),
        migrations.AlterModelTable(
            name='mechanic',
            table='shared_mechanic',
        ),
    ]
