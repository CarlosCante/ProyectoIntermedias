from django.contrib import admin
from .models import Usuario
from .models import Cliente
from .models import Bodega
from .models import Producto
from .models import Categoria
from .models import Sede

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Sede)