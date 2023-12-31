# Generated by Django 4.2.5 on 2023-10-05 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
        ('machine_parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='machinepart',
            name='image',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='machinepart',
            name='material',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='machinepart',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shared.mechanic'),
        ),
        migrations.AlterField(
            model_name='machinepart',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='machinepart',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
