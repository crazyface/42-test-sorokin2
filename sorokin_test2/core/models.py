from django.db import models

class Request(models.Model):
    path = models.TextField()
    status_code = models.PositiveIntegerField()
    method = models.CharField(max_length=10)
    params = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __unicode__(self):
        return '{0} at {1}'.format(self.path, self.created_at)