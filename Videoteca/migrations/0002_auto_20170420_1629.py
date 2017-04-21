# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Videoteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoteca',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Videoteca.Client'),
        ),
    ]
