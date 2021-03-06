# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('path_reg', models.CharField(max_length=128)),
            ],
            options={
                'permissions': (('access_to_Function', '进入功能'),),
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('isDel', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('do', models.CharField(max_length=128)),
                ('level', models.CharField(choices=[('warn', 'warn'), ('error', 'error'), ('fatal', 'fatal'), ('debug', 'debug'), ('info', 'info')], default='info', max_length=8)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('app', models.CharField(max_length=32)),
            ],
            options={
                'permissions': (('access_to_module', '进入模块'),),
            },
        ),
        migrations.AddField(
            model_name='function',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SystemManage.Module'),
        ),
    ]
