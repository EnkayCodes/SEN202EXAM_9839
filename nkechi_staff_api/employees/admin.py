from django.contrib import admin

# Register your models here.
from .models import Manager, Intern, Address

#admin.site.register(StaffBase)
admin.site.register(Manager)
admin.site.register(Intern)
admin.site.register(Address)
