# Generated by Django 4.1.7 on 2023-03-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_license_responsible_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='Expiry_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='license',
            name='Installation_Date',
            field=models.DateField(),
        ),
    ]