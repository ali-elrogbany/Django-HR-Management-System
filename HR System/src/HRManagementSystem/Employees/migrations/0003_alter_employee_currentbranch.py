# Generated by Django 4.2.2 on 2023-06-26 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Branches', '0004_alter_branch_manager'),
        ('Employees', '0002_employee_age_employee_email_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='currentBranch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Branches.branch'),
        ),
    ]
