from django import forms


class Calendar(forms.DateInput):

    def __init__(self, attrs=None, format=None):
        default_atts = {'class': 'datepicker',
                        'autocomplete':'off'}
        if attrs is not None:
            default_atts.update(attrs)
        return super(Calendar, self).__init__(attrs=default_atts,
                                              format=format)

    class Media:
        css = {
            'all': ('css/jquery-ui-1.8.21.custom.css',)
        }
        js = ('js/jquery-ui-1.8.21.custom.min.js', 'js/date_picker_init.js')
