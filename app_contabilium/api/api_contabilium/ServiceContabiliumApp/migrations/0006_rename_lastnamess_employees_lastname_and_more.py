# Generated by Django 4.1.4 on 2023-01-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceContabiliumApp', '0005_alter_companies_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='lastNamess',
            new_name='lastName',
        ),
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
