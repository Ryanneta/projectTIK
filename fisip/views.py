import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFisip(request):
    fisip = ["Program Studi Administrasi Publik", "Program Studi Ilmu Komunikasi", "Program Studi Ilmu Pemerintahan"]

    konteksFISIP = {
        'fisip' : fisip
    }
    return render(request, 'indexFisip.html', konteksFISIP)