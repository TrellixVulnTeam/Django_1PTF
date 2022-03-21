from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    a = range(1, 100)
    numbers = random.sample(a, 6)
    name = 'ssafy'
    context = {
        'numbers': numbers,
        'name': name,
    }
    return render(request, 'lotto.html', context)