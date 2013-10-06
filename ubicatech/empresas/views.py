# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from empresas.serializers import UserSerializer, GroupSerializer,EmpresaSerializer 
from rest_framework import generics
from empresas.models import Empresa

class UserViewSet(viewsets.ModelViewSet):
	"""
	API QUE PERMITE A LOS USUARIOS SER VISTOS Y EDITADOS
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API que permite a los grupos ser vistos y editados
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
	"""
     LISTA DE EMPRESAS
	"""
	queryset = Empresa.objects.all()
	serializer_class = EmpresaSerializer
