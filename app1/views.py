from django.shortcuts import render


def index(request):
    #we can pass dictionary as context to render
    context = {
        'name': 'Django',
        'version': '1.11'
    }
    return render(request, 'index.html', context)



def info(request):
    #we can pass dictionary as context to render
    context = {
        'name': 'Yugan',
        'age': '25'
    }
    return render(request, 'info.html', context)