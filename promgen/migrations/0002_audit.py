# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 05:36


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
