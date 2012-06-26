from django.contrib import admin
from sorokin_test2.accounts import models


class ProfileAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.Profile, ProfileAdmin)