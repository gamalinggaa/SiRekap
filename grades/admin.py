from django.contrib import admin
from .models import MataKuliah, Kelas, Mahasiswa, Quiz, NilaiQuiz

admin.site.register(MataKuliah)
admin.site.register(Kelas)
admin.site.register(Mahasiswa)
admin.site.register(Quiz)
admin.site.register(NilaiQuiz)