# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legislator',
            fields=[
                ('official_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='littlebro.Official')),
            ],
            options={
            },
            bases=('littlebro.official',),
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('official_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='littlebro.Official')),
            ],
            options={
            },
            bases=('littlebro.official',),
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('official_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='littlebro.Official')),
                ('badge_number', models.IntegerField()),
            ],
            options={
            },
            bases=('littlebro.official',),
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('rank', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['rank'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.SlugField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='police',
            name='rank',
            field=models.ForeignKey(to='littlebro.Rank'),
            preserve_default=True,
        ),
    ]
