# Generated by Django 4.0.6 on 2022-08-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0009_verification_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pquantity', models.CharField(max_length=100)),
            ],
        ),
    ]
