# Generated by Django 4.2.2 on 2023-06-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branches', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='buildingNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
