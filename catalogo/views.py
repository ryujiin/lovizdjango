from django.shortcuts import render
from models import *
from serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import viewsets

class CategoriaViewsets(viewsets.ReadOnlyModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer	

class ProductoListaViewsets(viewsets.ModelViewSet):
	model = Producto
	serializer_class = ProductoListaSerializer

class Producto_singleViewstes(viewsets.ModelViewSet):
	serializer_class = ProductoSingleSereializer
	
	def get_queryset(self):
		queryset = Producto.objects.all()
		return queryset

class Producto_singleView(APIView):
	def get_object(self):
		slug = self.request.QUERY_PARAMS.get('slug', None)
		try:
			return Producto.objects.get(slug = slug)
		except Producto.DoesNotExist:
			raise Http404

	def get(self,request,format=None):
		producto = self.get_object()
		serializer = ProductoSingleSereializer(producto)
		return Response(serializer.data,status=status.HTTP_200_OK)


class CatalogoViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = ProductoListaSerializer

	def get_queryset(self):
		queryset = Producto.objects.filter(activo=True).order_by('-pk')
		categoria = self.request.QUERY_PARAMS.get('categoria', None)
		if categoria:
			queryset = Producto.objects.filter(activo=True,categorias__slug=categoria).order_by('-pk')
		return queryset

##Catalogo##

class ColorViewsets(viewsets.ReadOnlyModelViewSet):
	queryset = Color.objects.all()
	serializer_class = ColoresSerializers

class TallaViewsets(viewsets.ReadOnlyModelViewSet):
	queryset = Talla.objects.all()
	serializer_class = TallaSerializers
