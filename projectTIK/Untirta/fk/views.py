import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFK(request):
    fk = ["Program Studi Kedokteran", "Program Studi Keperawatan S1", "Program Studi Keperawatan D3", "Program Studi S1 Gizi", "Program Studi Ilmu Keolahragaan"]

    konteksFK = {
        'fk' : fk
    }

    return render(request, 'indexFK.html', konteksFK)