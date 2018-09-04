from django.contrib import admin

# Register your models here.
from flea_market.models import Inquiry, Event


@admin.register(Inquiry)
class MarketInquiryAdmin(admin.ModelAdmin):
    list_display = ['created', 'first_name', 'last_name', 'email', 'phone', 'paid']


@admin.register(Event)
class MarketEventAdmin(admin.ModelAdmin):
    list_display = ['start']
