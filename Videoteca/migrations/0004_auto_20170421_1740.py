# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videoteca', '0003_auto_20170421_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoteca',
            name='movies',
            field=models.ManyToManyField(to='Videoteca.Movie'),
        ),
    ]
