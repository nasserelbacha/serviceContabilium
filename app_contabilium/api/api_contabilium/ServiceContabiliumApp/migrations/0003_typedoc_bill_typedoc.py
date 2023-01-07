# Generated by Django 4.1.4 on 2023-01-04 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceContabiliumApp', '0002_remove_companies_employees_remove_providers_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDoc',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='typedoc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceContabiliumApp.typedoc'),
        ),
    ]