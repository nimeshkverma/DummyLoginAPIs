from __future__ import unicode_literals

from django.db import models


class DataLog(models.Model):
    log_type = models.CharField(
        max_length=50, blank=True, null=True)
    log_data = models.TextField(blank=False, null=False)

    class Meta(object):
        db_table = "data_log"

    def __unicode__(self):
        return '%s__%s' % (str(self.log_type), str(self.created_at))
