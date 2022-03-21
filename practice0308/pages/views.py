from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    a = range(1, 100)
    b = range(1, 6)
    numbers = random.sample(a, 6)
    bonus = random.sample(a, 1)
    winners = list(b)
    context = {
        'numbers': numbers,
        'bonus': bonus,
        'winners': winners,
    }
    return render(request, 'pages/lotto.html', context)