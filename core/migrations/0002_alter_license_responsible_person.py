# Generated by Django 4.0.6 on 2022-07-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='Responsible_person',
            field=models.CharField(choices=[('f', 'System Admin'), ('m', 'Network Admin'), ('o', 'Other')], max_length=11),
        ),
    ]