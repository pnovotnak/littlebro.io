# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littlebro', '0002_auto_20140928_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='district',
            field=models.ForeignKey(default=1, to='littlebro.District'),
            preserve_default=False,
        ),
    ]
