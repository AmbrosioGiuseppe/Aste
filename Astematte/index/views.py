from django.shortcuts import render
from Astematte.function import get_random_string_upp_dig

# Create your views here.
def index(request):
    a = get_random_string_upp_dig(6)
    print(a)
    context = {
        'a': a,
    }
    return render(request, 'index/index.html', context)


def asteConcluse(request):
    return render(request, 'index/index2.html')


def recensioni(request):
    return render(request, 'index/index2.html')

def comeFunziona(request):
    return render(request, 'index/index2.html')