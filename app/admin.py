from django.contrib import admin

# Register your models here.

from .models import USUARIO
from .models import ROL
from .models import ASIG_ROL
from .models import SEDE
from .models import BODEGA
from .models import CLIENTE
from .models import PRODUCTO
from .models import CATEGORIA_PRODUCTO
from .models import ASIG_CATEGORIA
from .models import ASIG_PRODUCTO
from .models import ORDEN_VENTA
from .models import LISTA_PRODUCTO
from .models import LOG_ACT_INVENTARIO

admin.site.register(USUARIO)
admin.site.register(ROL)
admin.site.register(ASIG_ROL)
admin.site.register(SEDE)
admin.site.register(BODEGA)
admin.site.register(CLIENTE)
admin.site.register(PRODUCTO)
admin.site.register(CATEGORIA_PRODUCTO)
admin.site.register(ASIG_CATEGORIA)
admin.site.register(ASIG_PRODUCTO)
admin.site.register(ORDEN_VENTA)
admin.site.register(LISTA_PRODUCTO)
admin.site.register(LOG_ACT_INVENTARIO)


