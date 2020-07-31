# Generated by Django 3.0.8 on 2020-07-31 08:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(unique=True)),
                ('status', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('stateid', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-code'],
            },
        ),
        migrations.CreateModel(
            name='UserCredentials',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)])),
                ('confirm_password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)])),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='ClientInformations',
            fields=[
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.UserCredentials')),
                ('fullname', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('address1', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(5)])),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='FuelQuotes',
            fields=[
                ('quoteid', models.AutoField(primary_key=True, serialize=False)),
                ('req_gallons', models.IntegerField()),
                ('del_address', models.CharField(max_length=100)),
                ('delivery_date', models.DateTimeField()),
                ('sugg_price', models.DecimalField(decimal_places=3, max_digits=9)),
                ('due_amount', models.DecimalField(decimal_places=3, max_digits=9)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserCredentials')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
