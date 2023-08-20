# Generated by Django 4.0.4 on 2022-05-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_rename_register_accounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Phone', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='accounts',
        ),
    ]
