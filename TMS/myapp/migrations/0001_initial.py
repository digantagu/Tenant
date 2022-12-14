# Generated by Django 4.0.6 on 2022-08-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('hid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('housename', models.CharField(max_length=122)),
                ('desc', models.CharField(max_length=122)),
                ('hrent', models.CharField(max_length=122)),
                ('type', models.CharField(max_length=122)),
                ('property', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseAllocation',
            fields=[
                ('hid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=122)),
                ('housename', models.CharField(max_length=12)),
                ('status', models.CharField(max_length=12)),
                ('deposit', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('lid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('spouse', models.CharField(max_length=122)),
                ('id', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('house', models.CharField(max_length=12)),
                ('hrent', models.CharField(max_length=122)),
                ('month', models.CharField(max_length=122)),
                ('amount', models.CharField(max_length=122)),
                ('balance', models.CharField(max_length=122)),
                ('status', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('pid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('hn', models.CharField(max_length=122)),
                ('landlord', models.CharField(max_length=122)),
                ('location', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('tid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('idtype', models.CharField(max_length=122)),
                ('idn', models.CharField(max_length=122)),
                ('dob', models.DateField()),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Turnover',
            fields=[
                ('tuid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('id', models.CharField(max_length=122)),
                ('amount', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
