# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-09 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='年纪'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(max_length=8, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author', verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=32, verbose_name='名称'),
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ManyToManyField(to='app01.Publish', verbose_name='出版社'),
        ),
    ]
