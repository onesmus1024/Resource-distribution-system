from django.contrib import admin
from .models import Importer, LocalSupplier, Consumer

# Register your models here.

admin.site.register(Importer)
admin.site.register(LocalSupplier)
admin.site.register(Consumer)
