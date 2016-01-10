# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='name',
            new_name='r_name',
        ),
    ]
