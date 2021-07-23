from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
class buku(models.Model):
	judul_buku = models.CharField(max_length=200,null=True)
	penulis = models.CharField(max_length=200,null=True)
	penerbit = models.CharField(max_length=200,null=True)
	tahun = models.IntegerField(null=True)
	def __str__(self):
		return self.judul_buku

class anggota(models.Model):
	nama = models.CharField(max_length=200,null=True)
	alamat = models.TextField(null=True)
	usia = models.IntegerField(null=True)
	def __str__(self):
		return self.nama

class data_pinjaman(models.Model):
	buku_key = models.ForeignKey(buku,models.SET_NULL,null=True,blank=True)
	anggota_key = models.ForeignKey(anggota,models.SET_NULL,null=True,blank=True)
	tanggal_pinjam = models.DateField(null=True,blank=True)
	tanggal_kembali = models.DateField(null=True,blank=True)
	def __str__(self):
		return self.buku_key