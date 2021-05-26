from django.contrib import admin
from .models import BankDetail
# Register your models here.
@admin.register(BankDetail)
class BankDetailAdmin(admin.ModelAdmin):
	list_display=['ifsc', 'bank_id', 'branch', 'city']