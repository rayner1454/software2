# -*- encoding: utf-8 -*-

# El siguiente formulario solo esta dirigido para  el tipo de cobro y para q aprendan a integrar ckeditor
from django import forms

from empresas.models import Tipo_de_cobro

from ckeditor.widgets import CKEditorWidget


class Tipo_de_cobroForm(forms.ModelForm):
	cod_tipo_cobro = forms.CharField(max_length=50)
	tipo_cobro = forms.CharField(max_length=50)
	descripcion = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Tipo_de_cobro