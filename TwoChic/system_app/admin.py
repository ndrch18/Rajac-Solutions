from django.contrib import admin
from .models  import RawMaterial, MaterialUnit, Account

admin.site.register(RawMaterial)
admin.site.register(MaterialUnit)
admin.site.register(Account)

