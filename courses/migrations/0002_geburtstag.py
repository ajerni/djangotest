# Generated by Django 4.2 on 2023-04-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geburtstag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=100)),
                ('nachname', models.CharField(max_length=100)),
                ('rufname', models.CharField(max_length=100)),
                ('geburtstag', models.CharField(max_length=100)),
            ],
        ),
    ]