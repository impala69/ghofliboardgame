# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-08 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Boardgame')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Boardgame')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Boardgame')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserWishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Boardgame')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User')),
            ],
        ),
    ]
