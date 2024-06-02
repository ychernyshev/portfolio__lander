from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'lander'
    }

    return render(request, 'lander/index.html', context=context)
