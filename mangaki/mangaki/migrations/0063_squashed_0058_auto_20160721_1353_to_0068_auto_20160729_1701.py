# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0062_auto_20160721_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anidb_language', models.CharField(blank=True, db_index=True, max_length=5)),
                ('iso639', models.CharField(db_index=True, max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaggedWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Tag')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
            ],
        ),
        migrations.CreateModel(
            name='WorkTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128)),
                ('type', models.CharField(blank=True, choices=[('main', 'principal'), ('official', 'officiel'), ('synonym', 'synonyme')], db_index=True, max_length=9)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Language')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='anidb_creator_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='work',
            name='tags',
            field=models.ManyToManyField(through='mangaki.TaggedWork', to='mangaki.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='taggedwork',
            unique_together=set([('work', 'tag')]),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]