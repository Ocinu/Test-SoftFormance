from django.shortcuts import render


def index(request):
    content = {
        'title': 'Main Page',
    }
    return render(request, 'index.html', content)
