from django.db import models
from django.conf import settings


class Job(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.IntegerField(default=0, choices=[(0, 'Unstarted'),
                                                     (1, 'Started'),
                                                     (2, 'Finished')])

    def status_class(self):
        return {0: '', 1: 'label-inverse', 2: 'label-success'}.get(self.status)

    def __unicode__(self):
        return u'Job #{0}'.format(self.id)


class Note(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, related_name='notes')

    def __unicode__(self):
        return u'Note #{0}'.format(self.id)
