from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.contrib.contenttypes.models import ContentType
from sorokin_test2.core.models import DbActivity
from django.db.utils import DatabaseError

exclude = [ContentType, DbActivity]


def create_update_handler(sender, instance, created, **kwargs):
    try:
        if sender in exclude:
            return
        ctype = ContentType.objects.get_for_model(sender)
        action = 'create' if created else 'update'
        DbActivity.objects.create(model=ctype,
                                  obj_pk=instance.pk,
                                  action=action)
    except DatabaseError:
        pass


def delete_handler(sender, instance, **kwargs):
    try:
        if sender in exclude:
            return
        ctype = ContentType.objects.get_for_model(sender)
        DbActivity.objects.create(model=ctype,
                                  obj_pk=instance.pk,
                                  action='delete')
    except DatabaseError:
        pass

post_save.connect(create_update_handler,
                  dispatch_uid='create_update')

post_delete.connect(delete_handler,
                  dispatch_uid='create_update')