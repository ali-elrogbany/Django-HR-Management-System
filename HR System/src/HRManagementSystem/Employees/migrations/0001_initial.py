# Generated by Django 4.2.2 on 2023-06-26 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('currentBranch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Branches.branch')),
            ],
        ),
    ]
