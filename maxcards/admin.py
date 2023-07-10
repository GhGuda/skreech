from django.contrib import admin
from .models import *

class CustomPaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'transaction_type', 'image',  'sent_on')



admin.site.register(User_orders)
admin.site.register(Cards)

admin.site.register(Payment_screenshot, CustomPaymentAdmin)