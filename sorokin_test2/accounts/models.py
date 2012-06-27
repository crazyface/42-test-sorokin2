from django.db import models


class Profile(models.Model):
    """General user information"""

    first_name = models.CharField(max_length=255, verbose_name='Name')
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    biography = models.TextField(verbose_name='Bio')
    email = models.EmailField(max_length=255)
    jabber = models.EmailField(max_length=255)
    skype = models.CharField(max_length=255)
    other_contacts = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)


    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
