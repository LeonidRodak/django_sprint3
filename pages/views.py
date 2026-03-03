from django.shortcuts import render


# Create your views here.
def about(request):
    """Страница «О проекте»"""
    return render(request, 'pages/about.html')


def rules(request):
    """Страница «Правила проекта»"""
    return render(request, 'pages/rules.html')
