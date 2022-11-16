from django.contrib import admin
from .models import Landlord, Property, House, Tenant, HouseAllocation, Payment, Turnover

admin.site.register(Landlord)
admin.site.register(Property)
admin.site.register(House)
admin.site.register(Tenant)
admin.site.register(HouseAllocation)
admin.site.register(Payment)
admin.site.register(Turnover)