#Creando seralizadores para los modelos 
#Usuario y grupos propios de Django
#Primero importamos los 2 modelos
from django.contrib.auth.models import User, Group

from empresas.models import Empresa, Sucursal
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
# Para ello creamos los serializadores de las sucurusales
class SucursalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sucursal
		fields = ('direccion','Ubicacion')
#Luego creamos el serializador para las empresas incorporando las sucursales
class EmpresaSerializer(serializers.ModelSerializer):
	sucursales = SucursalSerializer(many=True)
	class Meta:
		model = Empresa
		fields = ('cod_empresa','nombre','sucursales')