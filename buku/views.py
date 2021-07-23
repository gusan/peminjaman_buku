from django.shortcuts import render
from django.core.cache import cache
from .models import *
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
# @api_view(['GET', 'PUT','DELETE'])
class BukuViewSet(viewsets.ModelViewSet):
	queryset =  buku.objects.all()
	serializer_class = BukuSerializer

class AnggotaViewSet(viewsets.ModelViewSet):
	queryset = anggota.objects.all()
	serializer_class = AnggotaSerializer

class PinjamanViewSet(viewsets.ModelViewSet):
	queryset = data_pinjaman.objects.all()
	serializer_class = PinjamanSerializer


@api_view(['GET', 'POST'])
def peminjaman(request):   
	# mengambil semua data
	if request.method == 'GET':
		if 'data_pinjaman' in cache:
			data = cache.get('data_pinjaman')
			print('data from cache')
			serializer = PinjamanNestedSerializer(data, many=True)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			data = data_pinjaman.objects.all()
			serializer = PinjamanNestedSerializer(data, many=True)
			cache.set('data_pinjaman',data)
			print('data from db')
			return Response(serializer.data, status=status.HTTP_200_OK)
	# menambahkan data
	elif request.method == 'POST':
		serializer = PinjamanSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			cache.clear()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'PUT','DELETE','GET'])
def peminjamangetbyid(request,pk):
	try:
		data_pinjamans = data_pinjaman.objects.filter(id=pk)
	except data_pinjamans.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		if cache.get(pk):
			data_pinjamans = cache.get(pk)			
			print('data from cache')
			serializer = PinjamanNestedSerializer(data_pinjamans, many=True)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:			
			serializer = PinjamanNestedSerializer(data_pinjamans, many=True)
			cache.set(pk,data_pinjamans)
			print('data from db')
			return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = PinjamanNestedSerializer(data_pinjamans,data=request.data)				
		if serializer.is_valid():			
			serializer.save()
			cache.clear()
			print('delete from cache')
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		data_pinjamans.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		# coba
