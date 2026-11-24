from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def riwayat_nilai(request):
    return render(request, 'dashboard/riwayat_nilai.html')

def statistik(request):
    return render(request, 'dashboard/statistik.html')

def pengumuman(request):
    return render(request, 'dashboard/pengumuman.html')

def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

def data_mahasiswa(request):
    return render(request, 'dashboard/data_mahasiswa.html')

def data_kuis(request):
    return render(request, 'dashboard/data_kuis.html')

def kelola_nilai(request):
    return render(request, 'dashboard/kelola_nilai.html')

def admin_pengumuman(request):
    return render(request, 'dashboard/admin_pengumuman.html')
