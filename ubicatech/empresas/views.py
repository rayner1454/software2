# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from empresas.serializers import UserSerializer, GroupSerializer,EmpresaSerializer 
#from rest_framework import generics
from empresas.models import Empresa
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from empresas.forms import Tipo_de_cobroForm
def home_page():
	pass
def agregar_tipo_cobro(request):
    if request.method =="POST":
        formulario = Tipo_de_cobroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("index.html")
    else:
        formulario = Tipo_de_cobroForm()
    #Cambiar por las url a utilizar     
    return render_to_response("index.html",{'formulario':formulario},context_instance=RequestContext(request)) 

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
