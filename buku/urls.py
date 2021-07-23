from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from buku import views


urlpatterns = [    
    path('peminjaman/', views.peminjaman,name='peminjaman'),  
    path('peminjamangetbyid/<int:pk>/', views.peminjamangetbyid,name='peminjamangetbyid'),    
]

urlpatterns = format_suffix_patterns(urlpatterns)