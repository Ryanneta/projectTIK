import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFT(request):
    ft = ["Program Studi Teknik Elektro", "Program Studi Teknik Industri", "Program Studi Teknik Kimia", "Program Studi Teknik Mesin", "Program Studi Teknik Metalurgi", "Program Studi Teknik Sipil"]

    konteksFT = {
        'ft' : ft
    }    
    return render(request, 'indexFT.html', konteksFT)