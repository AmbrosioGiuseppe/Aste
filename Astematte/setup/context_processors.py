from setup.models import *

def setting(request):
    menu = Menu.objects.filter(attivo=True)

    context = {
        'menu': menu,
    }

    return context