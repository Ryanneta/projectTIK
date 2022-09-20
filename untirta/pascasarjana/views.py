import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiPC(request):
    pc = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"]

    konteksPC = {
        'pc' : pc
    }
    return render(request, 'indexPC.html', konteksPC)