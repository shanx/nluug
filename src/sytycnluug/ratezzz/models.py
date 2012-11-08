from django.db import models


class Talk(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    speakers = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0} by {1}'.format(self.name, self.speakers)

    def get_absolute_url(self):
        return '/ratezzz/{0}/'.format(self.pk)

