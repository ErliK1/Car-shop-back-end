# Generated by Django 4.2.5 on 2023-09-19 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shared', '0005_alter_biguser_table_alter_mechanic_table'),
        ('MachineParts', '0004_categorymachineparts_alter_machineparts_tags_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='machineparts',
            unique_together={('name', 'year', 'brand', 'owner')},
        ),
    ]