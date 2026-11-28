from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class MataKuliah(models.Model):
    kode = models.CharField(max_length=20, unique=True)  # Contoh: CSGE601020
    nama = models.CharField(max_length=100)              # Contoh: Dasar-Dasar Pemrograman 1

    def __str__(self):
        return f"{self.kode} - {self.nama}"


class Kelas(models.Model):
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name="daftar_kelas")
    nama_kelas = models.CharField(max_length=20)  # Contoh: DDP1-A sampai DDP1-I
    # Membatasi agar asisten dosen hanya bisa mengelola nilai di kelas tanggung jawabnya
    asdos = models.ManyToManyField(User, related_name="kelas_diampu", blank=True)

    class Meta:
        unique_together = ("mata_kuliah", "nama_kelas")

    def __str__(self):
        return self.nama_kelas


class Mahasiswa(models.Model):
    # Dihubungkan dengan sistem login SSO UI yang akan dibuat oleh G
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    npm = models.CharField(max_length=10, primary_key=True)
    nama = models.CharField(max_length=150)
    # Satu mahasiswa berada di tepat satu kelas untuk mata kuliah DDP1
    kelas = models.ForeignKey(Kelas, on_delete=models.PROTECT, related_name="mahasiswa")

    def __str__(self):
        return f"{self.npm} - {self.nama} ({self.kelas.nama_kelas})"


class Quiz(models.Model):
    # Terhubung ke Kelas karena setiap kelas memiliki jumlah dan soal kuis berbeda
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, related_name="quizzes")
    judul = models.CharField(max_length=50)  # Contoh: Quiz 1, Quiz 2
    tanggal = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ("kelas", "judul")
        ordering = ["id"]

    def __str__(self):
        return f"{self.kelas.nama_kelas} - {self.judul}"


class NilaiQuiz(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name="nilai_quiz")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="nilai_mahasiswa")
    nilai = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    # Mencatat alasan & waktu pembaruan jika mahasiswa mengajukan appeal nilai ke asdos
    catatan_appeal = models.TextField(blank=True, default="")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Memastikan satu kuis hanya memiliki satu nilai per mahasiswa
        unique_together = ("mahasiswa", "quiz")

    def __str__(self):
        return f"{self.mahasiswa.npm} | {self.quiz.judul}: {self.nilai}"