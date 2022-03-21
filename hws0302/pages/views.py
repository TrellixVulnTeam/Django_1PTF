from django.shortcuts import render

# Create your views here.
def dinner(request, menu, guests):
    context = {
        'menu': menu,
        'guests': guests,
    }
    return render(request, 'pages/dinner.html', context)