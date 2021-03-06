from django.db import models
from django.contrib.contenttypes.models import ContentType


class Request(models.Model):
    path = models.TextField()
    status_code = models.PositiveIntegerField()
    method = models.CharField(max_length=10)
    params = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    priority = models.IntegerField(max_length=1, default=0)

    class Meta:
        ordering = ('-created_at', )

    def __unicode__(self):
        return '{0} at {1}'.format(self.path, self.created_at)


class DbActivity(models.Model):
    ACTION_CHOICES = [['create', 'create'],
                      ['update', 'update'],
                      ['delete', 'delete']]

    model = models.ForeignKey(ContentType)
    obj_pk = models.CharField(max_length=255)
    action = models.CharField(max_length=30, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0} with pk {1} was {2} at {3}'.format(self.model,
                                                       self.obj_pk,
                                                       self.action,
                                                       self.created_at)