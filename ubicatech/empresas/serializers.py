#Creando seralizadores para los modelos 
#Usuario y grupos propios de Django
#Primero importamos los 2 modelos
from django.contrib.auth.models import User, Group

from empresas.models import Empresa
from rest_framework import serializers 

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields =('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Group
		fields = ('url', 'name')

#Creamos el serializador para la empresa 

class EmpresaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empresa
		#fields = ('nombre','ubicacion','imagen','servicios','proposito','fecha_registro','telefono','cantidad_sucursales')