from django.core.management.base import BaseCommand, CommandError
from django.db import models


class Command(BaseCommand):
    args = '<app_label.ModelName ...>'
    help = 'Show all project models and the count of objects in every model.'

    def handle(self, *args, **options):
        if args:
            show_models = []
            for arg in args:
                model = models.get_model(*arg.split('.'))
                if model is None:
                    raise CommandError('Model "{0}" does not exist.'.format(
                                                                        arg))
                show_models.append(model)
        else:
            show_models = models.get_models()
        for model in show_models:
            model_name = '{0}.{1}'.format(model._meta.app_label,
                                      model.__name__).rjust(30)
            output = '{0}: {1} objects\n'.format(model_name,
                                                  model.objects.count())
            self.stdout.write(output)
            self.stderr.write('error: ' + output)
