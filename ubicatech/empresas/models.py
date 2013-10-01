#encododing:utf-8 <-Permite usar tildes y caracteres

from django.db import models
# Es aqui donde definimos el modelo que tendra esta aplicacion 
#Un modelo es la representacion de los datos de nuestra aplicacion
#Contiene los campos  basicos y el comportamiento de los datos que seran almacenados

# A continacion creamos la clase Empresario, donde definimos los campos que tendra.

class Empresario(models.Model):
	ci = models.CharField(max_length=10)
	nombre = models.CharField(max_length=100)
	paterno = models.CharField(max_length=50)
	materno = models.CharField(max_length=50)
	nombre_usuario = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	correo_electronico = models.EmailField(max_length=75)
	celular = models.CharField(max_length=50)
	sexo = models.CharField(max_length=15)
	nacionalidad = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

#La siguiente clase almacena los tipos de cobro que se tendran, es decir define esta clase
#los diferentes precios de servicio para las empresas.
class  Tipo_de_cobro(models.Model):
	cod_tipo_cobro = models.CharField(max_length=50)
	tipo_cobro = models.CharField(max_length=50)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.tipo_cobro

# La clase mas importante es la clase Empresa, el cual tiene los siguientes campos necesarios para ofrecer nuestros servicios

class Empresa(models.Model):
	cod_empresa = models.CharField(max_length=50)
	nombre = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to ='empresa', verbose_name='Logo')
	servicios = models.CharField(max_length=100)
	proposito = models.CharField(max_length=100)
	fecha_registro = models.DateField()
	telefono = models.CharField(max_length=100)
	cantidad_sucursales = models.IntegerField(max_length=2)
	cod_tipo_cobro = models.ForeignKey(Tipo_de_cobro, related_name='Tipo_cobro')

	def  __unicode__(self):
		return self.nombre

# La siguiente clase declara la ubicacion exacta de una sucursal
# donde se toma la latitud y longitud para ubicarlo sobre un mapa de google Maps
class Sucursal(models.Model):
	cod_empresa = models.ForeignKey(Empresa)
	direccion = models.CharField(max_length=100)
	latitud = models.CharField(max_length=10)
	longitud = models.CharField(max_length=10)
    
	def  __unicode__(self):
		return "%s"%(self.id)
# A continuacion declaramos los tipos de pagos, es decir las maneras para pagar ya sea
# con paypal y Cuenta de Banco

class Tipo_de_pago(models.Model):
	tipo_pago = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)

	def  __unicode__(self):
		return "%s"%(self.id)


# A continuacion mediante la siguiente clase hacemos un seguimiento de los pagos 
# haga la empresa 
class Pagos(models.Model):
	cod_empresa = models.ForeignKey(Empresa, related_name='codigo')
	cod_tipo_cobro = models.ForeignKey(Empresa)
	tipo_pago = models.ForeignKey(Tipo_de_pago)
	monto_cancelado = models.FloatField()
	saldo = models.FloatField()

	def __unicode__(self):
		return self.cod_empresa

#A continuacion dedefinimos la clase actividad la cual contiene
# los datos mas relevantes del centro de entretenimiento, es decir los servicios 
# promociones, horarios de atencion entre otros.

class Actividad(models.Model):
	cod_empresa = models.ForeignKey(Empresa)
	descripcion = models.TextField()
	precio_entrada = models.FloatField()
	frase_del_dia = models.TextField()
	evento_principal = models.TextField()
	imagen = models.ImageField(upload_to ='empresa', verbose_name='Foto') # Provicionalmente esta la direccion de esta carpeta
	horario_de_atencion = models.CharField(max_length=100)
	fecha_de_actividad = models.DateField()

	def __unicode__(self):
		return self.cod_empresa


#OJO revisar la siguiente clase del estado de cuenta
class Estado_de_Cuenta(models.Model):
	cod_empresa = models.ForeignKey(Empresa)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.cod_empresa

# A continuacion creamos la clase que contiene los atribuitos 
# de un usuario que usa la aplicacion 

class Usuario(models.Model):
	ci = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	paterno = models.CharField(max_length=50)
	materno = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to ='empresa', verbose_name='Foto') # Provicionalmente esta la direccion de esta carpeta
	intereses = models.TextField()
	correo_electronico = models.EmailField(max_length=75)
	sexo = models.CharField(max_length=20)
	nacionalidad = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

#la siguiente clase registra todos los comentarios emitidos por los usuarios de una empresa
class Comentario(models.Model):
	cod_empresa= models.ForeignKey(Empresa)
	ci = models.ForeignKey(Usuario)
	comentario = models.TextField()

	def __unicode__(self):
		return self.comentario

# A continuacion la clase puntaje define la calificacion 
# que una persona da a una empresa 

class Puntaje(models.Model):
	cod_empresa= models.ForeignKey(Empresa)
	ci = models.ForeignKey(Usuario)
	puntaje = models.IntegerField()

	def __unicode__(self):
		return self.puntaje

# Finalmente la clase Visita registra todas las visitas

class Visita(models.Model):
	cod_empresa= models.ForeignKey(Empresa)
	ci = models.ForeignKey(Usuario)
	fecha = models.DateField()
	observaciones = models.TextField()








# Create your models here.
