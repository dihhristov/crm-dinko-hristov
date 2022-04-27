from django.contrib import admin

from crm.accounts.models import Profile, CrmUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", 'position')

@admin.register(CrmUser)
class CrmUserAdmin(admin.ModelAdmin):
    pass
