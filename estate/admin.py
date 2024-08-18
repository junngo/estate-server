from django.contrib import admin
from .models import AptTransaction

@admin.register(AptTransaction)
class AptTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'apt_nm', 'deal_year', 'deal_month', 'deal_day', 'deal_amount', 'sgg_cd', 'umd_nm', 'apt_dong', 'floor'
    )
    list_filter = ('deal_year', 'deal_month', 'sgg_cd', 'apt_nm')
    search_fields = ('apt_nm', 'sgg_cd', 'umd_nm', 'apt_dong')
