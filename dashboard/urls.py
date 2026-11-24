from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('riwayat-nilai/', views.riwayat_nilai, name='riwayat_nilai'),
    path('statistik/', views.statistik, name='statistik'),
    path('pengumuman/', views.pengumuman, name='pengumuman'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('data-mahasiswa/', views.data_mahasiswa, name='data_mahasiswa'),
    path('data-kuis/', views.data_kuis, name='data_kuis'),
    path('kelola-nilai/', views.kelola_nilai, name='kelola_nilai'),
    path('admin-pengumuman/', views.admin_pengumuman, name='admin_pengumuman'),

]