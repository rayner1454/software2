from django.contrib import admin

from empresas.models import Empresario, Tipo_de_cobro, Empresa, Sucursal, Tipo_de_pago, Pagos, Actividad, Estado_de_Cuenta, Usuario, Comentario, Puntaje,Visita

admin.site.register(Empresario)
admin.site.register(Tipo_de_cobro)
admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Tipo_de_pago)
admin.site.register(Pagos)
admin.site.register(Actividad)
admin.site.register(Estado_de_Cuenta)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Puntaje)
admin.site.register(Visita)