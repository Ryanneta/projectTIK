import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFH(request):
    fh = "Program Sarjana Ilmu Hukum"

    konteksFH = {
    'fh' : fh
    }

    return render(request, 'indexFH.html', konteksFH)