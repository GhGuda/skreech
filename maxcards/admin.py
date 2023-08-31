from django.contrib import admin
from .models import *

class CustomPaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'transaction_type', 'image',  'sent_on',)
    
    
class Customcard(admin.ModelAdmin):
    readonly_fields = ('card_id', )



admin.site.register(User_orders)
admin.site.register(Cards, Customcard)

admin.site.register(Payment_screenshot, CustomPaymentAdmin)