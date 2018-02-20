# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-19 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description_override', models.TextField(blank=True, max_length=500, verbose_name='SEO: Meta description override')),
                ('title_override', models.CharField(blank=True, max_length=120, verbose_name='SEO: Title override')),
                ('block_indexing', models.BooleanField(default=False, verbose_name='SEO: Block indexing by search engine robots')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('slug', models.SlugField(help_text='"Slug" is a part of an url adress.', max_length=140, unique=True)),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
