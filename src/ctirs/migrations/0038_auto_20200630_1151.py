# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-30 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctirs', '0037_feed_stix_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='sharing_range_type',
            field=models.CharField(choices=[('all', 'With all'), ('group', 'With a group'), ('people', 'With people')], default='all', max_length=10),
        ),
        migrations.AlterField(
            model_name='stipuser',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('pt-br', 'Portuguese'), ('es', 'Spanish'), ('ja', 'Japanese'), ('fr', 'French'), ('zh-cn', 'Chinese')], default='en', max_length=16),
        ),
        migrations.AlterField(
            model_name='group',
            name='locale',
            field=models.CharField(choices=[('en', 'English'), ('pt-br', 'Portuguese'), ('es', 'Spanish'), ('ja', 'Japanese'), ('fr', 'French'), ('zh-cn', 'Chinese')], default='en', max_length=4),
        ),
    ]
