# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-26 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0094_auto_20180508_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqentry',
            options={'verbose_name_plural': 'FAQ entries'},
        ),
        migrations.AlterModelOptions(
            name='faqtheme',
            options={'verbose_name_plural': 'FAQ themes'},
        ),
        migrations.AlterField(
            model_name='relatedwork',
            name='type',
            field=models.CharField(choices=[('', 'Unknown'), ('prequel', 'Prequel'), ('sequel', 'Sequel'), ('summary', 'Summary'), ('side_story', 'Side story'), ('parent_story', 'Parent story'), ('alternative_setting', 'Alternative setting'), ('same_setting', 'Same setting'), ('other', 'Special'), ('adaptation', 'Adaptation')], default='', max_length=20, verbose_name='Type de relation'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='message',
            field=models.TextField(blank=True, verbose_name='Suggestion'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='problem',
            field=models.CharField(choices=[('title', 'Wrong title'), ('poster', 'Wrong poster'), ('synopsis', 'Synopsis contains mistakes'), ('author', 'Wrong author'), ('composer', 'Wrong composer'), ('double', 'This is a duplicate'), ('nsfw', 'Work is Not Safe for Work'), ('n_nsfw', 'Work is actually Safe for Work'), ('ref', 'Suggest a reference URL (MyAnimeList, AniDB, Icotaku, VGMdb, etc.)')], default='ref', max_length=8, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='top',
            name='category',
            field=models.CharField(choices=[('directors', 'Directors'), ('authors', 'Authors'), ('composers', 'Composers')], max_length=10, unique_for_date='date'),
        ),
        migrations.AlterField(
            model_name='work',
            name='manga_type',
            field=models.TextField(blank=True, choices=[('seinen', 'Seinen'), ('shonen', 'Shonen'), ('shojo', 'Shojo'), ('yaoi', 'Yaoi'), ('sonyun-manhwa', 'Sonyun-Manhwa'), ('kodomo', 'Kodomo'), ('ecchi-hentai', 'Ecchi-Hentai'), ('global-manga', 'Global-Manga'), ('manhua', 'Manhua'), ('josei', 'Josei'), ('sunjung-sunjeong', 'Sunjung-Sunjeong'), ('chungnyun', 'Chungnyun'), ('yuri', 'Yuri'), ('dojinshi-parodie', 'Dojinshi-Parody'), ('manhwa', 'Manhwa'), ('yonkoma', 'Yonkoma')], max_length=16),
        ),
        migrations.AlterField(
            model_name='work',
            name='origin',
            field=models.CharField(blank=True, choices=[('japon', 'Japan'), ('coree', 'Korea'), ('france', 'France'), ('chine', 'China'), ('usa', 'US'), ('allemagne', 'Germany'), ('taiwan', 'Taiwan'), ('espagne', 'Spain'), ('angleterre', 'UK'), ('hong-kong', 'Hong Kong'), ('italie', 'Italia'), ('inconnue', 'Unknown'), ('intl', 'International')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='workcluster',
            name='status',
            field=models.CharField(choices=[('unprocessed', 'Unprocessed'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='unprocessed', max_length=11),
        ),
    ]