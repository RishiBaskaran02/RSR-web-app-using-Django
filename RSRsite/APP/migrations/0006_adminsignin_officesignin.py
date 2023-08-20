# Generated by Django 4.0.4 on 2022-07-29 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_signin_delete_accounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminsignin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Phone', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeSignin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Phone', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]