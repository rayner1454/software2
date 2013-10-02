from django.contrib import admin

from empresas.models import Empresario, Tipo_de_cobro, Empresa, Sucursal, Tipo_de_pago, Pagos, Actividad, Estado_de_Cuenta, Usuario, Comentario, Puntaje,Visita

# A continuacion modificamos el admin Django 

class EmpresarioAdmin(admin.ModelAdmin):
	fieldsets = [('Datos de Informacion', {'fields': ['ci','nombre','paterno','materno','nombre_usuario','password','correo_electronico','celular','sexo','nacionalidad']}),
    ]
	search_fields = ['nombre','paterno','materno','correo_electronico','celular','sexo','nacionalidad']
	list_display = ('nombre','paterno','materno','correo_electronico','celular','sexo','nacionalidad')
	list_filter = ['nombre','paterno','materno','correo_electronico','celular','sexo','nacionalidad']


admin.site.register(Empresario,EmpresarioAdmin)
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