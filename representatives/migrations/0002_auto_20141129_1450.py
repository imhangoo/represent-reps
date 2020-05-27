# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

class JSONField(models.TextField):
    """Mocks jsonfield 0.92's column-type behaviour"""
    def db_type(self, connection):
        if connection.vendor == 'postgresql' and connection.pg_version >= 90300:
            return 'json'
        else:
            return super(JSONField, self).db_type(connection)


class Migration(migrations.Migration):

    dependencies = [
        ('representatives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='extra',
            field=JSONField(default=dict, blank=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='offices',
            field=JSONField(default=dict, blank=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='extra',
            field=JSONField(default=dict, blank=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='offices',
            field=JSONField(default=dict, blank=True),
        ),
    ]
