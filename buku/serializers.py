from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

class BukuSerializer(serializers.ModelSerializer):
	class Meta:
		model = buku
		fields = '__all__'
		#menampilkan semua field pada class Album

class AnggotaSerializer(serializers.ModelSerializer):
	class Meta:
		model = anggota
		fields = '__all__'

class PinjamanSerializer(serializers.ModelSerializer):
	class Meta:
		model = data_pinjaman
		fields = '__all__'		

class PinjamanNestedSerializer(WritableNestedModelSerializer):
	buku_key = BukuSerializer()
	anggota_key = AnggotaSerializer()
	class Meta:
		model = data_pinjaman
		# fields = '__all__'
		fields = ['id','tanggal_pinjam','tanggal_kembali','buku_key','anggota_key']