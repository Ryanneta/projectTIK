import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFaper(request):
    faper = ["Program Studi Agribisnis", "Program Studi Agroekoteknologi", "Program Studi Ilmu Perikanan", "Program Studi Teknologi Pangan"]

    konteksFAPER = {
        'faper' : faper
    }

    return render(request, 'indexFaper.html', konteksFAPER)