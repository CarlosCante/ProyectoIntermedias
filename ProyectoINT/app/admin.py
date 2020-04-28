from django.contrib import admin
from .models import Usuario
from .models import Cliente
from .models import Bodega

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Bodega)