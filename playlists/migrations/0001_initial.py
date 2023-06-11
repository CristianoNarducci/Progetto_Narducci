# Generated by Django 4.2.1 on 2023-05-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_modified', models.DateTimeField(verbose_name='date modified')),
            ],
        ),
    ]
