# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littlebro', '0003_rank_district'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='police',
            options={'verbose_name_plural': 'Police'},
        ),
        migrations.AddField(
            model_name='police',
            name='image',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
