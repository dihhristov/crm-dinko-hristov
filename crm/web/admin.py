from django.contrib import admin

from crm.web.models import Customers, Contracts, Offers, Tasks


@admin.register(Customers)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Contracts)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Tasks)
class ProfileAdmin(admin.ModelAdmin):
    pass
