import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFEB(request):
    feb = ["Program Sarjana Managemen", "Program Sarjana Akuntansi", "Program Sarjana Ilmu Ekonomi Pembangunan", "Program Sarjana Ekonomi Syariah",     "Program Diploma III Akuntansi", "Program Diploma III Marketing", "Program Diploma III Perpajakan", "Program Diploma III Keuangan Perbankan"]

    konteksFEB = {
        'feb' : feb
    }

    return render(request, 'index.html', konteksFEB)