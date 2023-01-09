# Generated by Django 4.1.4 on 2023-01-08 13:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(default='hola@gmail.com', max_length=233)),
                ('password', models.CharField(default='', max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDoc',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=233)),
                ('lastNamess', models.CharField(default='', max_length=233)),
                ('email', models.EmailField(default='hola@gmail.com', max_length=233)),
                ('password', models.CharField(default='', max_length=233)),
                ('isAdmin', models.BooleanField(default=False)),
                ('company', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceContabiliumApp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=233)),
                ('coordate_x', models.IntegerField(default=1)),
                ('coordate_y', models.IntegerField(default=1)),
                ('info', models.CharField(default='', max_length=233)),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceContabiliumApp.companies')),
                ('provider', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceContabiliumApp.providers')),
                ('typedoc', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceContabiliumApp.typedoc')),
            ],
        ),
    ]
